from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Auth(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    created_date = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="auth")