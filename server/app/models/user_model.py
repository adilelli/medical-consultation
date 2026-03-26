from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    role = Column(Integer)
    created_date = Column(DateTime, server_default=func.now())

    doctor_consultations = relationship("Consultation", foreign_keys="Consultation.doctor_id", back_populates="doctor")
    patient_consultations = relationship("Consultation", foreign_keys="Consultation.patient_id", back_populates="patient")
    auth = relationship("Auth", uselist=False, back_populates="user", cascade="all, delete-orphan")