from app.repositories.diagnosis_repository import DiagnosisRepository
from app.schemas.consultation_schema import ConsultationCreate

class DiagnosisService:
    def __init__(self, repo: DiagnosisRepository):
        self.repo = repo

    async def list_diagnosis(self):
        return await self.repo.get_diagnosis()
    
    async def list_diagnosis_by_name(self, name: str):
        return await self.repo.get_diagnosis_by_name(name)