from pydantic import BaseModel
from typing import List


class User(BaseModel):
    login = str
    password = str
    class Config():
        orm_mode = True

class Item(BaseModel):
    name : str
    price : float
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    login = str
    password = str
    items : List[Item] = []
    class Config():
        orm_mode = True

class ShowItem(BaseModel):
    name : str
    price : float
    owner : User
    class Config():
        orm_mode = True