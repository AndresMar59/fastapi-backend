from fastapi import FastAPI
from dotenv import load_dotenv
from app.Brex.router import router as brex_router


app = FastAPI()

# Registrar routers
app.include_router(brex_router)
