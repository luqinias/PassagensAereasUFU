from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base
import json

class Aeroportos(Base):
    __tablename__ = 'aeroportos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True, nullable=False)    
    cidade = Column(String(50), unique=True, nullable=False)
    estado = Column(String(50), nullable=False)

