from pydantic import BaseModel
from typing import List

class Bakugan(BaseModel):
    nombre: str
    atributo: str
    poder: int
    cartas: List[str]
    fortalezas: List[str]
    debilidades: List[str]
    imagen: str
