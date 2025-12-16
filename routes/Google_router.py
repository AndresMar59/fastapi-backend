from app.Google.Service import read
from fastapi import APIRouter

router = APIRouter()

@router.get("/costos/Google")
def Costo(range: str):

    sheet_id = "1NTdiIrjbj4o5cqq2L4SLta5fNniQ4g5mjkNLazKMbqk"
    range_ = "'V0'!" + range

    return read(sheet_id, range_)