from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ConsultationCreate(BaseModel):
    doctor_id: int
    patient_id: int
    description: str

class UserSimple(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class ConsultationResponse(BaseModel):
    id: int
    doctor: UserSimple
    patient: UserSimple
    description: str
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)