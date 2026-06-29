import os
import json
from typing import List, Optional
from models import Bakugan

class BakuganRepository:
    def __init__(self, filename: str = "bakugan.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "data", filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"[!] No se encontró el archivo: {path}")

        with open(path, "r", encoding="utf-8") as f:
            self.__bakugans: List[Bakugan] = [Bakugan(**b) for b in json.load(f)]

    def get_all(self) -> List[Bakugan]:
        return self.__bakugans
    
    def get_by_name(self, nombre: str) -> Optional[Bakugan]:
        return next((b for b in self.__bakugans if b.nombre.lower() == nombre.lower()), None)
