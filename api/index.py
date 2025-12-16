from fastapi import FastAPI
from mangum import Mangum
from .routes.Brex_router import router as brex_router
from .routes.Google_router import router as google_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="Mi API FastAPI",
    description="API funcionando en Vercel",
    version="1.0.0"
)

# Ruta principal
@app.get("/")
def read_root():
    return {
        "message": "API funcionando en Vercel",
        "status": "ok"
    }

# Registrar routers
app.include_router(brex_router)
app.include_router(google_router)


# Handler para Vercel - DEBE estar al final
handler = Mangum(app, lifespan="off")
