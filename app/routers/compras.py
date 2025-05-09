from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.compras import CompraRequest, CompraResponse
from crud import compras as crud_compras
from models.database import get_db

router = APIRouter(prefix="/compras", tags=["Compras"])

@router.post("/", response_model=CompraResponse)
def efetuar_compra(compra: CompraRequest, db: Session = Depends(get_db)):
    resultado = crud_compras.efetuar_compra(db, compra)

    if not resultado:
        raise HTTPException(status_code=400, detail="Compra não realizada. Verifique disponibilidade.")

    return resultado
