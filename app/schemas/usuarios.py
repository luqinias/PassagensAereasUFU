from pydantic import BaseModel

class Usuarios(BaseModel):
    nome: str
    idade: int
    telefone: str
    cidade: str
    estado: str
    endereco: str
    email: str
    senha: str
    