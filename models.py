from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = ""



@dataclass
class Product:
    name: str
    price: float
    description: str
    url: str
