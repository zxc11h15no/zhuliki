from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class accounting(BaseModel):
    id: Optional[int]
    eventID: int
    income: int
    costs: int
    drugs: str

class drugs(BaseModel):
    id: Optional[int]
    quantity: int
    for_sale: int
    for_personal_use: int

class share(BaseModel):
    id: Optional[int]
    accountingID: int
    memberID: int
    part: int

class User(BaseModel):
    login: str
    password: str
    post: Optional[int]
    reg_date: Optional[datetime]






