from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.auth_model import Auth
from app.models.user_model import User
from app.schemas.auth_schema import AuthCreate
from app.schemas.user_schema import UserCreate, UserResponse
from sqlalchemy import select

class AuthRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_auth(self, auth: AuthCreate):
        db_auth = Auth(
            **auth.model_dump()
        )
        self.db.add(db_auth)
        await self.db.commit()
        await self.db.refresh(db_auth)
        return db_auth
    
    async def get_auth_by_id(self, user_id: str):
        result = await self.db.execute(select(Auth).where(Auth.user_id == user_id))
        return result.scalar_one_or_none()