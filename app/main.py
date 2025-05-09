from fastapi import FastAPI
from auth import auth as auth_router
from app.models.aeroportos import Aeroportos
from app.models.usuarios import Usuarios
from app.models.passagens import Passagens
from app.models.voos import Voos
from app.schemas.aeroportos import Aeroportos
from app.schemas.usuarios import Usuarios
from app.schemas.passagens import Passagens 
from app.schemas.voos import Voos
from app.routers import aeroportos, passagens, voos, compras
from models.database import Base, engine
from datetime import datetime
import json

app = FastAPI(
    title="Gerenciador de Passagens Aereas - UFU",
    description="API para gerenciamento de passagens."
)

app.include_router(auth_router.router)
app.include_router(aeroportos.router, prefix="/api")
app.include_router(passagens.router, prefix="/api")
app.include_router(voos.router, prefix="/api")
app.include_router(compras.router, prefix="/api")


#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@app.get("/aeroportos")
def read_aeroportos():
    return {"message": "Aeroportos disponiveis!"}

@app.get("/passagens")
def read_aeroportos():
    return {"message": "Passagens disponiveis!"}


