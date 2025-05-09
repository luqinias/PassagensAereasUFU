from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    senha: str

class LoginResponse(BaseModel):
    chave_sessao: str

class SessaoStatus(BaseModel):
    ativa: bool
    mensagem: str
