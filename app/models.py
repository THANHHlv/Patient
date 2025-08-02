from sqlalchemy import Column, Integer, String, Date
from .database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    day_in = Column(Date, nullable=True)
    hos_fee = Column(Integer, nullable=True)
