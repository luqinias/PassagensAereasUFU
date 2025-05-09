from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), unique=True , nullable=False)
    idade = Column(Integer, nullable=False)
    telefone = Column(String(20), nullable=False)
    estado = Column(String(2))
    cidade = Column(String(40))
    endereco = Column(String(100))
    email = Column(String(20), unique=True, nullable=False)
    senha = Column(String(20), nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    

