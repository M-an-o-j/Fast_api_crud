from pydantic import BaseModel
from database.models import Item
from typing import List

class ItemCreate(BaseModel):
    name : str
    description: str = None
    price:float
    tax:float

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str = None
    price:float
    tax:float

class ItemUpdate(BaseModel):
    name: str
    description: str = None
    price:float
    tax:float

# class ItemList(BaseModel):
#     items: List[Item]

#     class config:
#         orm_mode = True