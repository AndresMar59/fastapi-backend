import requests
from dotenv import load_dotenv
import os

load_dotenv()


# No es necesario la clase, dado que solo hay un token. La instancia no ocupa parametro
class BrexClient:
    BASE_URL = "https://platform.brexapis.com"

    def __init__(self):
        BREX_TOKEN = os.getenv("BREX_TOKEN") #Esto es parte del contructor de la clase
        self.headers = {"Authorization": f"Bearer {BREX_TOKEN}"}

    def paginated(self, params, ruta):
        """
        Llama a Brex y resuelve la paginación correctamente.
        """
        all_results = []
        next_cursor = None
# La API de Brex usa paginación por cursor.
        while True:
            query_params = params.copy()

            if next_cursor:
                query_params["cursor"] = next_cursor

            response = requests.get( f"{self.BASE_URL}{ruta}",
                headers=self.headers,
                params=query_params,
            )

            print("STATUS:", response.status_code)
            print("RAW TEXT:", response.text[:500])

            if response.status_code != 200:
                raise Exception(
                    f"Error desde Brex: {response.status_code} - {response.text}"
                )

            try:
                data_json = response.json()
            except:
                raise Exception(f"Brex no devolvió JSON válido: {response.text}")

            # La data viene en: data_json["items"]
            items = data_json.get("items", [])
            all_results.extend(items)

            # Cursor correcto viene en: data_json["next_cursor"]
            next_cursor = data_json.get("next_cursor")
            if not next_cursor:
                break

        return all_results


    def get_Icome_paginated(self, params, ruta, id:str):
        """
        Llama a Brex y resuelve la paginación correctamente.
        """
        all_results = []
        next_cursor = None
# La API de Brex usa paginación por cursor.
        while True:
            query_params = params.copy()

            if next_cursor:
                query_params["cursor"] = next_cursor

            response = requests.get( f"{self.BASE_URL}{ruta}",
                headers=self.headers,
                params=query_params,
            )

            print("STATUS:", response.status_code)
            print("RAW TEXT:", response.text[:500])

            if response.status_code != 200:
                raise Exception(
                    f"Error desde Brex: {response.status_code} - {response.text}"
                )

            try:
                data_json = response.json()
            except:
                raise Exception(f"Brex no devolvió JSON válido: {response.text}")

            # La data viene en: data_json["items"]
            items = data_json.get("items", [])
            all_results.extend(items)

            # Cursor correcto viene en: data_json["next_cursor"]
            next_cursor = data_json.get("next_cursor")
            if not next_cursor:
                break

        return all_results































