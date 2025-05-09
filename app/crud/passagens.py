from sqlalchemy.orm import Session
from models.passagens import Passagens as passagens_models
from schemas.passagens import Passagens as passagens_schemas

def criar_passagem(db: Session, passagem: passagens_schemas):
    nova_passagem = passagens_models(**passagem.dict())
    db.add(nova_passagem)
    db.commit()
    db.refresh(nova_passagem)
    return nova_passagem

def listar_passagens(db: Session, skip: int = 0, limit: int = 10):
    return db.query(passagens_models).offset(skip).limit(limit).all()

def buscar_passagem(db: Session, passagem_id: int):
    return db.query(passagens_models).filter(passagens_models.id == passagem_id).first()

def deletar_passagem(db: Session, passagem_id: int):
    passagem = db.query(passagens_models).filter(passagens_models.id == passagem_id).first()
    if passagem:
        db.delete(passagem)
        db.commit()
    return passagem
