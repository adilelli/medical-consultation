from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    name: str
    role: int

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)