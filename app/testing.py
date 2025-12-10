import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://platform.brexapis.com/v1/expenses/card"
headers = {
    "Authorization": f"Bearer {os.getenv('BREX_TOKEN')}"
}

param = {"purchased_at_start":"2025-08-31T23:59:59.999", "purchased_at_end": "2025-09-01T23:59:59.999"
}
resp = requests.get(url, headers=headers,params=param)

print(resp.status_code)
print(resp.text)