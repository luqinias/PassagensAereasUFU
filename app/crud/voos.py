from sqlalchemy.orm import Session
from models.voos import Voos as voos_models
from schemas.voos import Voos as voos_schemas
from models.aeroportos import Aeroportos as aeroportos_models


def criar_voos(db: Session, voos: voos_schemas):
    novo_voo = voos_models(**voos.dict())
    db.add(novo_voo)
    db.commit()
    db.refresh(novo_voo)
    return novo_voo

def listar_voos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(voos_models).offset(skip).limit(limit).all()

def buscar_voos_por_id(db: Session, voos_id: int):
    return db.query(voos_models).filter(voos_models.origem_id == voos_id).first()

def buscar_voos_por_data(db: Session, voos_data: str):
    return db.query(voos_models).filter(voos_models.data_origem == voos_data).all()

def deletar_voos(db: Session, voos_id: int):
    voos = db.query(voos_models).filter(voos_models.origem_id == voos_id).first()
    if voos:
        db.delete(voos)
        db.commit()
    return voos

def listar_destinos_por_origem(db: Session, origem_id: int):
    voos = db.query(voos_models).filter(voos_models.origem_id == origem_id).all()
    destinos_ids = list({voo.destino_id for voo in voos})
    return db.query(aeroportos_models).filter(aeroportos_models.id.in_(destinos_ids)).all()

def pesquisar_voos(db: Session, origem_id: int, destino_id: int, passageiros: int):
    return db.query(voos_models).filter(
        voos_models.origem_id == origem_id,
        voos_models.destino_id == destino_id,
        voos_models.assentos_disponiveis >= passageiros
    ).order_by(voos_models.tarifa.asc()).all()
