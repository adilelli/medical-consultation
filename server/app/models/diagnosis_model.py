from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base
from sqlalchemy.sql import func

class Diagnosis(Base):
    __tablename__ = "diagnosis"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    description = Column(String)
    created_date = Column(DateTime, server_default=func.now())