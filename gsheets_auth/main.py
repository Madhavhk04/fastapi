import os
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import bcrypt
from models import UserCreate
from sheets_service import GoogleSheetsService

app = FastAPI(title="Google Sheets User Directory")

# Spreadsheet Config - Replace with your actual Spreadsheet ID
SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID", "1JRyZHM3vTJcbu9Tc3jE3E0feqpx5sUpfpdChfcuamwA")
SHEET_NAME = "Sheet1"
RANGE_NAME = f"{SHEET_NAME}!A:D"

sheets_service = GoogleSheetsService(spreadsheet_id=SPREADSHEET_ID)

def get_password_hash(password):
    # Truncate to 72 bytes to satisfy bcrypt limitations
    password_bytes = password.encode('utf-8')[:72]
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode('utf-8')

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/register")
async def register_user(user: UserCreate):
    try:
        # Hash password before storing
        hashed_password = get_password_hash(user.password)
        
        # Automatically generate created_at timestamp
        created_at = datetime.now(timezone.utc).isoformat()
        
        # Prepare row data match columns: email | password | role | created_at
        row_data = [user.email, hashed_password, user.role, created_at]
        
        # Append to Google Sheet
        sheets_service.append_row(RANGE_NAME, row_data)
        
        return JSONResponse(content={"message": "User registered successfully!"}, status_code=201)
    except Exception as e:
        # Return proper JSON responses to avoid frontend unhandled errors
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/users")
async def get_users():
    try:
        rows = sheets_service.get_rows(RANGE_NAME)
        
        if not rows:
            return JSONResponse(content={"users": []})
        
        # Skip header row if the first column header exists and equals 'email' (case-insensitive)
        if rows and len(rows[0]) > 0 and rows[0][0].lower() == "email":
            rows = rows[1:]
            
        users = []
        for row in rows:
            # Handle empty cells to avoid index out of bounds
            email = row[0] if len(row) > 0 else ""
            role = row[2] if len(row) > 2 else ""
            created_at = row[3] if len(row) > 3 else ""
            
            # We never return passwords to frontend
            users.append({
                "email": email,
                "role": role,
                "created_at": created_at
            })
            
        return JSONResponse(content={"users": users})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
