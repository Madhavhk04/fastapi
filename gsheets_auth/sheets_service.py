import os
import certifi
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Handling SSL certificate issues on Windows
os.environ['SSL_CERT_FILE'] = certifi.where()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_FILE = 'credentials (2).json'

class GoogleSheetsService:
    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.credentials = None
        self.service = None
        self._authenticate()

    def _authenticate(self):
        try:
            if os.path.exists(CREDENTIALS_FILE):
                self.credentials = Credentials.from_service_account_file(
                    CREDENTIALS_FILE, scopes=SCOPES
                )
                self.service = build('sheets', 'v4', credentials=self.credentials)
            else:
                print(f"Warning: {CREDENTIALS_FILE} not found. Google Sheets API will not work.")
        except Exception as e:
            print(f"Error authenticating with Google Sheets: {e}")

    def append_row(self, range_name: str, row_data: list):
        if not self.service:
            self._authenticate()
        if not self.service:
            raise Exception("Google Sheets service not authenticated. Credentials file may be missing or invalid.")
        body = {
            'values': [row_data]
        }
        result = self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id, range=range_name,
            valueInputOption='USER_ENTERED', body=body).execute()
        return result

    def get_rows(self, range_name: str):
        if not self.service:
            self._authenticate()
        if not self.service:
            raise Exception("Google Sheets service not authenticated. Credentials file may be missing or invalid.")
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        return values
