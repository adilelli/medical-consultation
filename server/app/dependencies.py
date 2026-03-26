from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.auth_repository import AuthRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.repositories.diagnosis_repository import DiagnosisRepository
from app.services.diagnosis_service import DiagnosisService
from app.repositories.consultation_repository import ConsultationRepository
from app.services.consultation_service import ConsultationService

def get_user_service(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    auth_repo = AuthRepository(db)
    return UserService(repo, auth_repo)

def get_diagnosis_service(db: Session = Depends(get_db)):
    repo = DiagnosisRepository(db)
    return DiagnosisService(repo)

def get_consultation_service(db: Session = Depends(get_db)):
    repo = ConsultationRepository(db)
    user = UserRepository(db)
    diagnosis = DiagnosisRepository(db)
    return ConsultationService(repo, user, diagnosis)

def get_auth_service(db: Session = Depends(get_db)):
    auth_repo = AuthRepository(db)
    user_repo = UserRepository(db)
    return AuthService(auth_repo, user_repo)
