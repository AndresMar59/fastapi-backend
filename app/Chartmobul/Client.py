import chartmogul
from dotenv import load_dotenv
import os

load_dotenv()

CHARTMOGUL_API_KEY = os.getenv("CHARTMOGUL_API_KEY")
config = chartmogul.Config(api_key=CHARTMOGUL_API_KEY)

response = chartmogul.Ping.ping(config)
print(response.get())
