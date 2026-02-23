# Google Sheets Auth Registration System

This project is a complete production-ready FastAPI system utilizing Google Sheets as a database database for a user registration structure. 

## Requirements
- Python 3.9+ 
- A Google Service Account with **Google Sheets API** enabled.

## Setup Instructions

1. **Install Dependencies**
   Navigate to the project directory and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Google Service Account Credentials**
   - Head over to the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the **Google Sheets API**.
   - Create a Service Account, generate a JSON key, and download it.
   - Rename that downloaded file to `credentials.json` and place it in the root directory here (`fastapi/gsheets_auth/credentials.json`).
   - Open your target Google Sheet.
   - Click "Share" in the top right, and share it with the Client Email found inside your `credentials.json`. Give it "Editor" permissions.

3. **Google Sheet Structure Setup**
   Ensure your spreadsheet has the columns exactly corresponding to this format. Make sure "Sheet1" is your working sheet, and enter row 1 exactly as:
   - Cell A1: `email`
   - Cell B1: `password`
   - Cell C1: `role`
   - Cell D1: `created_at`

4. **Environment Configuration**
   By default, you can set the `SPREADSHEET_ID` environment variable to your Google Sheet ID (the long characters inside the URL of your Google Sheet doc). Alternatively, simply edit `main.py` and replace:
   ```python
   SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID", "YOUR_SPREADSHEET_ID_HERE")
   ```

5. **Run the Application**
   Run the FastAPI server using Uvicorn:
   ```bash
   python main.py
   ```
   Or via uvicorn command directly:
   ```bash
   uvicorn main:app --reload
   ```

6. **Usage**
   Open your browser and navigate to exactly:
   `http://localhost:8000/`

   You will instantly see the frontend fetching the API correctly, displaying your sheet users and providing an interactive system avoiding missing undefined errors!
