from sqlalchemy import String, Integer, Column, Float, TIMESTAMP, text, ForeignKey
from .database import Base
from .aeroportos import Aeroportos
from .usuarios import Usuarios
from .voos import Voos
import json

class Passagens(Base):
    __tablename__ = 'passagens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), ForeignKey('usuarios.nome'))    
    tarifa = Column(Float, ForeignKey('voos.tarifa'), nullable=False)
    hora_origem = Column(String(50), ForeignKey('voos.hora_origem') ,nullable=False)
    data_origem = Column(String(50), ForeignKey('voos.data_origem') ,nullable=False)
    aeroporto_origem = Column(String(50), ForeignKey('aeroportos.nome'))
    aeroporto_destino = Column(String(50), ForeignKey('aeroportos.nome'))
    aeroporto_origem_cidade = Column(String(50), ForeignKey('aeroportos.cidade'))
    aeroporto_destino_cidade = Column(String(50), ForeignKey('aeroportos.cidade'))

