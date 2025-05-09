import uuid
from sqlalchemy.orm import Session
from models.compras import Compra
from models.voos import Voos

def efetuar_compra(db: Session, compra_data):
    voo = db.query(Voos).filter(Voos.origem_id == compra_data.voo_id).first()

    if not voo or voo.assentos_disponiveis < compra_data.quantidade_passageiros:
        return None

    voo.assentos_disponiveis -= compra_data.quantidade_passageiros

    localizador = str(uuid.uuid4())[:8]
    e_tickets = [str(uuid.uuid4())[:12] for _ in range(compra_data.quantidade_passageiros)]

    nova_compra = Compra(
        voo_id=compra_data.voo_id,
        nome_comprador=compra_data.nome_comprador,
        documento_comprador=compra_data.documento_comprador,
        localizador=localizador,
    )

    db.add(nova_compra)
    db.commit()

    return {"localizador": localizador, "e_tickets": e_tickets}
