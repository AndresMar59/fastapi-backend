from fastapi import APIRouter, HTTPException
from datetime import datetime
from urllib.parse import unquote
from app.Brex.Service import costos_CAC, costos_UE
from datetime import timezone, datetime

router = APIRouter(prefix="/brex")


def validar_fecha_rfc3339(fecha_str: str, nombre: str):
    try:
        dt = datetime.fromisoformat(fecha_str.replace("Z", "+00:00"))
    except:
        raise HTTPException(400, f"{nombre} no tiene formato RFC3339 válido")

    # Si la fecha es naive (sin tzinfo), asumir UTC
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    return dt

@router.get("/CAC")
def Costo_CAC(start_date: str, end_date: str | None = None, acumulado: bool | None =None):

    if end_date is None:
     end_date = datetime.now(timezone.utc).isoformat()

    # 1. Decodificar parámetros (por si vienen URL encoded)
    start_date = unquote(start_date)
    end_date = unquote(end_date)

# 2. Validar fechas en formato RFC 3339
    fecha_inicio = validar_fecha_rfc3339(start_date, "start_date")
    fecha_fin = validar_fecha_rfc3339(end_date, "end_date")

    if fecha_inicio >= fecha_fin:
       raise HTTPException(
        status_code=400,
        detail="start_date debe ser menor que end_date"
    )

    return costos_CAC(start_date, end_date, acumulado)


@router.get("/UE")
def Costo_UE(start_date: str, end_date: str | None = None, acumulado: bool | None = None ):

    if end_date is None:
     end_date = datetime.now(timezone.utc).isoformat()

    # 1. Decodificar parámetros (por si vienen URL encoded)
    start_date = unquote(start_date)
    end_date = unquote(end_date)

# 2. Validar fechas en formato RFC 3339
    fecha_inicio = validar_fecha_rfc3339(start_date, "start_date")
    fecha_fin = validar_fecha_rfc3339(end_date, "end_date")

    if fecha_inicio >= fecha_fin:
       raise HTTPException(
        status_code=400,
        detail="start_date debe ser menor que end_date"
    )

    return costos_UE( start_date, end_date, acumulado)
