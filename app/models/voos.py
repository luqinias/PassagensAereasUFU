from sqlalchemy import String, Integer, Column, Float, TIMESTAMP, text, ForeignKey
from .database import Base
from .aeroportos import Aeroportos
import json


class Voos(Base):
    __tablename__ = 'voos'
    origem_id = Column(Integer, primary_key=True, autoincrement=True)
    destino_id = Column(Integer, ForeignKey('aeroportos.id'), nullable=False)
    tarifa = Column(Float, unique=True, nullable=False)
    assentos_disponiveis = Column(Integer, nullable=False)
    data_origem = Column(String(50), unique=True, nullable=False)
    data_destino = Column(String(50), nullable=False)
    hora_origem = Column(String(50), unique=True, nullable=False)
    hora_destino = Column(String(50), nullable=False)
    aeroporto_origem = Column(String(50), ForeignKey('aeroportos.nome'), nullable=False)
    aeroporto_destino = Column(String(50), ForeignKey('aeroportos.nome'), nullable=False)
    aeroporto_origem_cidade = Column(String(50), ForeignKey('aeroportos.cidade'), nullable=False)
    aeroporto_destino_cidade = Column(String(50), ForeignKey('aeroportos.cidade'), nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

