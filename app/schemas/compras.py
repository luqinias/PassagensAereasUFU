from pydantic import BaseModel
from typing import List

class CompraRequest(BaseModel):
    voo_id: int
    quantidade_passageiros: int
    nome_comprador: str
    documento_comprador: str

class CompraResponse(BaseModel):
    localizador: str
    e_tickets: List[str]
