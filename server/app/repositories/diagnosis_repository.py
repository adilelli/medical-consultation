from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.diagnosis_model import Diagnosis
from app.schemas.diagnosis_schema import DiagnosisResponse
from sqlalchemy import select

class DiagnosisRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    # async def create_consultation(self, consultation: ConsultationCreate):
    #     db_write = Consultation(**consultation.model_dump())
    #     self.db.add(db_write)
    #     await self.db.commit()
    #     await self.db.refresh(db_write)
    #     return db_write

    async def get_diagnosis(self):
        result = await self.db.execute(select(Diagnosis))
        return result.scalars().all()
    

    async def get_diagnosis_by_name(self, name:str):
        stmt = (select(Diagnosis).where(Diagnosis.description.ilike(f"%{name}%")))
        result = await self.db.execute(stmt)
        return result.scalars().all()