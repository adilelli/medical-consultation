from enum import IntEnum
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class AuthCreate(BaseModel):
    user_id: int
    hashed_password: str


class AuthResponse(BaseModel):
    id: int
    user_id: int
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)