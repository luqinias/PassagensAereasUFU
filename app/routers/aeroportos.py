from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import aeroportos as crud_aeroportos
from crud import voos as crud_voos
from schemas.aeroportos import Aeroportos as aeroportos_schemas
from models.aeroportos import Aeroportos as aeroportos_models

from models.database import get_db

router = APIRouter(prefix="/aeroportos", tags=["Aeroportos"])

@router.post("/", response_model=aeroportos_schemas)
def criar_aeroporto(aeroporto: aeroportos_schemas, db: Session = Depends(get_db)):
    return crud_aeroportos.criar_aeroporto(db, aeroporto)

@router.get("/", response_model=list[aeroportos_schemas])
def listar_aeroportos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_aeroportos.listar_aeroportos(db, skip, limit)

@router.get("/{aeroporto_id}", response_model=aeroportos_schemas)
def buscar_aeroporto(aeroporto_id: int, db: Session = Depends(get_db)):
    aeroporto = crud_aeroportos.buscar_aeroporto(db, aeroporto_id)
    if not aeroporto:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    return aeroporto

@router.delete("/{aeroporto_id}")
def deletar_aeroporto(aeroporto_id: int, db: Session = Depends(get_db)):
    aeroporto = crud_aeroportos.deletar_aeroporto(db, aeroporto_id)
    if not aeroporto:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    return {"ok": True}

@router.get("/destinos/{origem_id}", response_model=list[aeroportos_schemas])
def listar_destinos_por_origem(origem_id: int, db: Session = Depends(get_db)):
    destinos = crud_voos.listar_destinos_por_origem(db, origem_id)
    if not destinos:
        raise HTTPException(status_code=404, detail="Nenhum destino encontrado para esta origem")
    return destinos