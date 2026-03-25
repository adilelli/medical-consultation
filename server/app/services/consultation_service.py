from app.repositories.consultation_repository import ConsultationRepository
from app.repositories.user_repository import UserRepository
from app.schemas.consultation_schema import ConsultationCreate

class ConsultationService:
    def __init__(self, repo: ConsultationRepository, user: UserRepository):
        self.repo = repo
        self.user = user

    async def create_consultation(self, consultation: ConsultationCreate):
        doctor = await self.user.get_user_by_id(consultation.doctor_id)
        if doctor is None:
            raise ValueError("Doctor ID does not exist")
        
        patient = await self.user.get_user_by_id(consultation.patient_id)
        if patient is None:
            raise ValueError("Patient ID does not exist")
        
        db_consultation = await self.repo.create_consultation(consultation)

        db_consultation.doctor = doctor
        db_consultation.patient = patient

        return db_consultation

    async def get_consultations(self, name: str | None = None):
        if name:
            return await self.repo.get_consultation_by_name(name)
        return await self.repo.get_consultation()

