from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    doctor = relationship("User", foreign_keys=[doctor_id], back_populates="doctor_consultations")
    patient = relationship("User", foreign_keys=[patient_id], back_populates="patient_consultations")

    description = Column(String)
    created_date = Column(DateTime, server_default=func.now())