from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import passagens as crud_passagens
from schemas.passagens import Passagens as passagens_schema
from models.database import get_db

router = APIRouter(prefix="/passagens", tags=["Passagens"])

@router.post("/", response_model=passagens_schema)
def criar_passagem(passagem: passagens_schema, db: Session = Depends(get_db)):
    return crud_passagens.criar_passagem(db, passagem)

@router.get("/", response_model=list[passagens_schema])
def listar_passagens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_passagens.listar_passagens(db, skip, limit)

@router.get("/{passagem_id}", response_model=passagens_schema)
def buscar_passagem(passagem_id: int, db: Session = Depends(get_db)):
    db_passagem = crud_passagens.buscar_passagem(db, passagem_id)
    if not db_passagem:
        raise HTTPException(status_code=404, detail="Passagem não encontrada")
    return db_passagem

@router.delete("/{passagem_id}")
def deletar_passagem(passagem_id: int, db: Session = Depends(get_db)):
    passagem = crud_passagens.deletar_passagem(db, passagem_id)
    if not passagem:
        raise HTTPException(status_code=404, detail="Passagem não encontrada")
    return {"ok": True}
