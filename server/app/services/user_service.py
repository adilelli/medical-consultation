from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, user: UserCreate):
        return await self.repo.create_user(user)

    async def list_users(self):
        return await self.repo.get_users()