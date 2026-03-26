from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserResponse
from sqlalchemy import select

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserCreate):
        db_user = User(
            **user.model_dump(exclude={"password"})
        )
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def get_users(self):
        result = await self.db.execute(select(User))
        return result.scalars().all()
    
    async def get_users_by_role(self, role: str):
        result = await self.db.execute(select(User).where(User.role == role))
        return result.scalars().all()

    async def get_user_by_email(self, email: str):
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_user_by_id(self, id: str):
        result = await self.db.execute(select(User).where(User.id == id))
        return result.scalar_one_or_none()