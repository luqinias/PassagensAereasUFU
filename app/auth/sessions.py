import uuid
from datetime import datetime, timedelta

sessoes_ativas = {}

def criar_sessao(email: str, ip: str):
    chave = str(uuid.uuid4())
    sessoes_ativas[chave] = {
        "email": email,
        "ip": ip,
        "expira_em": datetime.now() + timedelta(hours=1)
    }
    return chave

def encerrar_sessao(chave: str):
    return sessoes_ativas.pop(chave, None) is not None

def validar_sessao(chave: str, ip: str):
    sessao = sessoes_ativas.get(chave)
    if not sessao:
        return False, "Sessao nao encontrada"
    if sessao["ip"] != ip:
        return False, "IP invalido"
    if datetime.now() > sessao["expira_em"]:
        return False, "Sessao expirada"
    return True, "Sessao valida"
