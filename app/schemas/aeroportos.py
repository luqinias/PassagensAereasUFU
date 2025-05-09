from pydantic import BaseModel
	
class Aeroportos(BaseModel):
    id: int
    nome: str
    cidade: str
    estado: str