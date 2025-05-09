from fastapi import APIRouter, Request, HTTPException
from auth.schemas import LoginRequest, LoginResponse, SessaoStatus
from auth.sessions import criar_sessao, encerrar_sessao, validar_sessao

router = APIRouter(prefix="/auth", tags=["Autenticacao"])

@router.post("/login", response_model=LoginResponse)
def login(request_data: LoginRequest, request: Request):
    if request_data.email == "teste@teste.com" and request_data.senha == "123":
        ip = request.client.host
        chave = criar_sessao(request_data.email, ip)
        return {"chave_sessao": chave}
    raise HTTPException(status_code=401, detail="Credenciais invalidas")

@router.post("/logout")
def logout(chave_sessao: str):
    if not encerrar_sessao(chave_sessao):
        raise HTTPException(status_code=404, detail="Sessao nao encontrada")
    return {"mensagem": "Sessao encerrada com sucesso"}

@router.get("/validar", response_model=SessaoStatus)
def validar(chave_sessao: str, request: Request):
    ip = request.client.host
    valida, mensagem = validar_sessao(chave_sessao, ip)
    return {"ativa": valida, "mensagem": mensagem}
