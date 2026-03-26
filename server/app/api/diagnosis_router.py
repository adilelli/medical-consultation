from fastapi import APIRouter, Depends
from app.core.auth import get_current_user
from app.schemas.diagnosis_schema import DiagnosisResponse
from app.services.diagnosis_service import DiagnosisService
from app.dependencies import get_diagnosis_service

router = APIRouter(prefix="/diagnoses", tags=["Diagnoses"])

@router.get("/", response_model=list[DiagnosisResponse])
async def get_diagnosis_by_name(
    search: str | None = None,
    service: DiagnosisService = Depends(get_diagnosis_service),
    current_user: str = Depends(get_current_user)
):
    if search:
        return await service.list_diagnosis_by_name(search)
    return await service.list_diagnosis()