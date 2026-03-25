from sqlalchemy.orm import Session, selectinload, aliased
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.consultation_model import Consultation
from app.models.user_model import User
from app.schemas.consultation_schema import ConsultationCreate, ConsultationResponse
from sqlalchemy import select, or_

class ConsultationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_consultation(self, consultation: ConsultationCreate):
        db_write = Consultation(**consultation.model_dump())
        self.db.add(db_write)
        await self.db.commit()
        await self.db.refresh(db_write)
        return db_write

    async def get_consultation(self):
        result = await self.db.execute(select(Consultation).options(selectinload(Consultation.doctor), selectinload(Consultation.patient)))
        return result.scalars().all()
    
    async def get_consultation_by_name(self, name: str):
        Doctor = aliased(User)
        Patient = aliased(User)
        stmt = (
            select(Consultation)
            .join(Doctor, Consultation.doctor)
            .join(Patient, Consultation.patient)
            .options(
                selectinload(Consultation.doctor),
                selectinload(Consultation.patient)
            )
            .where(or_(Doctor.name.ilike(f"%{name}%"), Patient.name.ilike(f"%{name}%")))
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()