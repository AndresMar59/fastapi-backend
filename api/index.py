from fastapi import FastAPI
from dotenv import load_dotenv
from mangum import Mangum
from app.Brex.router import router as brex_router
from app.Google.router import router as google_router


app = FastAPI()

# Registrar routers
app.include_router(brex_router)
app.include_router(google_router)

@app.get("/")
def root():
    return {"message": "API funcionando en Vercel"}

# Handler para Vercel
handler = Mangum(app)