from fastapi import APIRouter, Depends
from app.schemas.consultation_schema import ConsultationCreate, ConsultationResponse
from app.services.consultation_service import ConsultationService
from app.dependencies import get_consultation_service
from app.core.auth import get_current_user

router = APIRouter(prefix="/consultations", tags=["Consultations"])

@router.post("/", response_model=ConsultationResponse)
async def create_consultation(
    consultation: ConsultationCreate,
    service: ConsultationService = Depends(get_consultation_service),
    current_user: str = Depends(get_current_user)
):
    return await service.create_consultation(consultation)

@router.get("/", response_model=list[ConsultationResponse])
async def get_consultation(
    search: str | None = None,
    service: ConsultationService = Depends(get_consultation_service),
    current_user: str = Depends(get_current_user)
):
    if search:
        return await service.get_consultations(search)
    
    return await service.get_consultations()

# @router.get("/", response_model=list[ConsultationResponse])
# async def get_consultation_by_user(
#     search: str,
#     service: ConsultationService = Depends(get_consultation_service)
# ):
#     return await service.list_consultation_by_user(search)

