from app.repositories.consultation_repository import ConsultationRepository
from app.repositories.diagnosis_repository import DiagnosisRepository
from app.repositories.user_repository import UserRepository
from app.schemas.consultation_schema import ConsultationCreate
from app.core.exceptions import UnauthorizedError, ForbiddenError, BusinessLogicError

class ConsultationService:
    def __init__(self, repo: ConsultationRepository, user: UserRepository, diagnosis: DiagnosisRepository):
        self.repo = repo
        self.user = user
        self.diagnosis = diagnosis

    async def create_consultation(self, consultation: ConsultationCreate):
        doctor = await self.user.get_user_by_id(consultation.doctor_id)
        if doctor is None:
            raise BusinessLogicError("Doctor ID does not exist")
        
        patient = await self.user.get_user_by_id(consultation.patient_id)
        if patient is None:
            raise BusinessLogicError("Patient ID does not exist")
        
        diagnosis = await self.diagnosis.get_diagnosis_by_id(consultation.diagnosis_id)
        if diagnosis is None:
            raise BusinessLogicError("Diagnosis ID does not exist")

        db_consultation = await self.repo.create_consultation(consultation)

        db_consultation.doctor = doctor
        db_consultation.patient = patient
        db_consultation.diagnosis = diagnosis

        return db_consultation

    async def get_consultations(self, name: str | None = None):
        if name:
            return await self.repo.get_consultation_by_name(name)
        return await self.repo.get_consultation()

