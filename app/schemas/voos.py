from pydantic import BaseModel
	
class Voos(BaseModel):
    origem_id: int
    destino_id: int
    tarifa: float
    assentos_disponiveis: int
    data_origem: str
    data_destino: str
    hora_origem: str
    hora_destino: str
    aeroporto_origem: str
    aeroporto_destino: str
    aeroporto_origem_cidade: str
    aeroporto_destino_cidade: str

class Config:
        from_attributes = True



    
    