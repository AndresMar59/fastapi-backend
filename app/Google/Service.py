from app.Google.Client import GoogleSheetsClient
import os

def read(sheet_id, range_):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        KEY_FILE = os.path.join(BASE_DIR, "service-account.json")
        client = GoogleSheetsClient(KEY_FILE)
        selft = client.cred()

        # result es un diccionario 
        result = selft.values().get(
            spreadsheetId=sheet_id,
            range=range_
        ).execute()
        
        values = result.get("values", [])
        if not values:
         return []

        headers = [h.strip() if isinstance(h, str) else h for h in values[0]]
        n_cols = len(headers)

        dicts = []
        for row in values[1:]:
        # Rellenar row hasta n_cols con None
          row_extended = row + [None] * (n_cols - len(row))
          row_extended = row_extended[:n_cols]
          obj = {headers[i]: row_extended[i] for i in range(n_cols)}
          dicts.append(obj)
        return dicts


