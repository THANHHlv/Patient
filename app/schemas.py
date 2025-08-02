from pydantic import BaseModel
from datetime import date


class PatientCreate(BaseModel):
    id: int
    name: str
    gender: str
    birth_date: date
    phone: str
    address: str
    day_in: date
    hos_fee: int


class PatienrUpdate(BaseModel):
    id: int
    name: str
    gender: str
    birth_date: date
    phone: str
    address: str
    day_in: date
    hos_fee: int
