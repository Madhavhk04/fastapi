# FastAPI Projects Collection

This repository contains two simple FastAPI applications:

## 1. Candidate Qualification API (`main.py`)
A single-file FastAPI application that connects to a PostgreSQL database to query for "qualified candidates" who possess a specific set of skills (Python, Tableau, and PostgreSQL).

### Usage
- Run the server: `uvicorn main:app --reload`
- Access the endpoint: `GET /qualified-candidates`

## 2. Google Sheets Authentication API (`gsheets_auth/`)
A more comprehensive FastAPI project demonstrating how to use Google Sheets as a lightweight database for user registration. 

### Features
- Serves a simple HTML frontend (`index.html`).
- API endpoint to register users (`POST /api/register`), which hashes passwords using `bcrypt` before storing them.
- API endpoint to fetch registered users (`GET /api/users`), stripping out sensitive information like passwords.
- Integrates with Google Sheets API to store and retrieve data.

### Setup
1. Navigate to the `gsheets_auth` directory.
2. Install requirements: `pip install -r requirements.txt`
3. Place your Google Sheets Service Account credentials in a `.json` file (ignored by git for security).
4. Update the `SPREADSHEET_ID` in `main.py` to point to your Google Sheet.
5. Run the server: `uvicorn main:app --reload`
