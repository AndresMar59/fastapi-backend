from fastapi import APIRouter, HTTPException
from datetime import datetime
from urllib.parse import unquote
from ..app.Brex.Service import costos_CAC, costos_UE
from datetime import timezone, datetime

router = APIRouter(prefix="/brex")


@router.get("/CAC")
def Costo_CAC(start_date: str, end_date: str | None = None, acumulado: bool | None =None):

    if end_date is None:
     end_date = datetime.now(timezone.utc).isoformat()

    # 1. Decodificar parámetros (por si vienen URL encoded)
    start_date = unquote(start_date)
    end_date = unquote(end_date)


    if  start_date>= end_date:
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

    if start_date >= end_date:
       raise HTTPException(
        status_code=400,
        detail="start_date debe ser menor que end_date"
    )

    return costos_UE( start_date, end_date, acumulado)
