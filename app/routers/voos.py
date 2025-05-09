from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from crud import aeroportos as crud_aeroportos
from crud import voos as crud_voos
from schemas.voos import Voos as voos_schema
from schemas.aeroportos import Aeroportos as aeroportos_schema
from models.database import get_db


router = APIRouter(prefix="/voos", tags=["Voos"])

@router.post("/", response_model=voos_schema)
def criar_voos(voos: voos_schema, db: Session = Depends(get_db)):
    return crud_voos.criar_voos(db, voos)

@router.get("/", response_model=list[voos_schema])
def listar_voos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_voos.listar_voos(db, skip, limit)

@router.get("/id/{voos_id}", response_model=voos_schema)
def buscar_voos_por_id(voos_id: int, db: Session = Depends(get_db)):
    db_voos = crud_voos.buscar_voos_por_id(db, voos_id)
    if not db_voos:
        raise HTTPException(status_code=404, detail="Voo não encontrado")
    return db_voos

@router.delete("/{voos_id}")
def deletar_voos(voos_id: int, db: Session = Depends(get_db)):
    voos = crud_voos.deletar_voos(db, voos_id)
    if not voos:
        raise HTTPException(status_code=404, detail="Voo não encontrado")
    return {"ok": True}

@router.get("/data/{voos_data}", response_model=list[voos_schema])
def buscar_voos_por_data(voos_data: str, db: Session = Depends(get_db)):
    db_voos = crud_voos.buscar_voos_por_data(db, voos_data)
    if not db_voos:
        raise HTTPException(status_code=404, detail="Nenhum voo encontrado na data informada")
    return db_voos

@router.get("/pesquisar", response_model=list[voos_schema])
def pesquisar_voos(
    origem_id: int,
    destino_id: int,
    passageiros: int,
    db: Session = Depends(get_db)
):
    voos = crud_voos.pesquisar_voos(db, origem_id, destino_id, passageiros)
    if not voos:
        raise HTTPException(status_code=404, detail="Nenhum voo disponivel para os criterios informados")
    return voos





