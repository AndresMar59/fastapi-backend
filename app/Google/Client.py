from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "service-account.json"
SHEET_ID = "1NTdiIrjbj4o5cqq2L4SLta5fNniQ4g5mjkNLazKMbqk"
RANGE = "Class Data!A2:E"

class GoogleSheetsClient:
    def __init__(self, key_file):
        self.creds = Credentials.from_service_account_file(
            key_file, scopes=SCOPES # este scope es solo para lectura. No se puede escribir nada
        )
        
    def cred(self):   
        self.service = build("sheets", "v4", credentials=self.creds)
        self.sheet = self.service.spreadsheets()
        return self.sheet
        


  







