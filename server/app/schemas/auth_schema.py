from dataclasses import Field
from enum import IntEnum
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime


class AuthCreate(BaseModel):
    user_id: int
    hashed_password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20, pattern="^[a-zA-Z0-9]*$")

class AuthResponse(BaseModel):
    id: int
    user_id: int
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)