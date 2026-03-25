from fastapi import APIRouter, Depends
from app.schemas.diagnosis_schema import DiagnosisResponse
from app.services.diagnosis_service import DiagnosisService
from app.dependencies import get_diagnosis_service

router = APIRouter(prefix="/diagnoses", tags=["Diagnoses"])

@router.get("/", response_model=list[DiagnosisResponse])
async def get_diagnosis_by_name(
    search: str | None = None,
    service: DiagnosisService = Depends(get_diagnosis_service)
):
    if search:
        return await service.list_diagnosis_by_name(search)
    return await service.list_diagnosis()