from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str = ""

@dataclass
class Order:
    product: str
    price: float
    price: float
    description: str
    url: str
    data: str

@dataclass
class Product:
    name: str
    price: float
    description: str
    url: str
