import json
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

class GoogleSheetsClient:
    def __init__(self):
        raw_json = os.getenv("GOOGLE_CREDENTIALS")

        if not raw_json:
            raise ValueError("GOOGLE_CREDENTIALS no está configurada en las variables de entorno")

        # Convertir JSON (string) → diccionario
        creds_dict = json.loads(raw_json)

        # Crear credenciales desde diccionario
        self.creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=SCOPES
        )

    def cred(self):
        service = build("sheets", "v4", credentials=self.creds)
        sheet = service.spreadsheets()
        return sheet

  







