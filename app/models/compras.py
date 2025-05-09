from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
    voo_id = Column(Integer, ForeignKey("voos.origem_id"))
    nome_comprador = Column(String)
    documento_comprador = Column(String)
    localizador = Column(String, unique=True)

    voo = relationship("Voos") 
