from pydantic import BaseModel

class TiendaSchema(BaseModel):
    id: int
    nombre: str