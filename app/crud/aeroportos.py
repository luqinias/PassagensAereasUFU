from sqlalchemy.orm import Session
from schemas.aeroportos import Aeroportos as aeroportos_schemas
from models.aeroportos import Aeroportos as aeroportos_models

def criar_aeroporto(db: Session, aeroporto: aeroportos_schemas):
    novo_aeroporto = aeroportos_models(**aeroporto.dict())
    db.add(novo_aeroporto)
    db.commit()
    db.refresh(novo_aeroporto)
    return novo_aeroporto

def listar_aeroportos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(aeroportos_models).offset(skip).limit(limit).all()

def buscar_aeroporto(db: Session, aeroporto_id: int):
    return db.query(aeroportos_models).filter(aeroportos_models.id == aeroporto_id).first()

def deletar_aeroporto(db: Session, aeroporto_id: int):
    aeroporto = db.query(aeroportos_models).filter(aeroportos_models.id == aeroporto_id).first()
    if aeroporto:
        db.delete(aeroporto)
        db.commit()
    return aeroporto
