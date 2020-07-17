from enum import Enum
from pydantic import BaseModel


class ProductStatus(str, Enum):
    bad = 'Bad'
    new = 'New'
    semi_new = 'Semi-new'


class ProductBase(BaseModel):
    name: str
    status: ProductStatus
    price: int
    picture: str
    location: str


class ProductOnBD(ProductBase):
    id_: str
