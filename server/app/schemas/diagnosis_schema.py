from pydantic import BaseModel, ConfigDict

# class DiagnosisCreate(BaseModel):
#     doctor: str
#     patient: str
#     description: str

class DiagnosisResponse(BaseModel):
    id: int
    code: str
    description: str

    model_config = ConfigDict(from_attributes=True)