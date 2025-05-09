from pydantic import BaseModel
	
class Passagens(BaseModel):
    nome: str
    tarifa: float
    hora_origem: str
    data_origem: str
    aeroporto_origem: str
    aeroporto_destino: str
    aeroporto_origem_cidade: str
    aeroporto_destino_cidade: str


    
    
    


