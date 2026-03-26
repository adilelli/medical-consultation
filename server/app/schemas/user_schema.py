from enum import IntEnum
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserRole(IntEnum):
    DOCTOR = 1
    PATIENT = 2

class UserCreate(BaseModel):
    email: str
    name: str
    role: UserRole


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    created_date: datetime
    role: UserRole

    model_config = ConfigDict(from_attributes=True)