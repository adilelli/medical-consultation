from app.core.security import hash_password
from app.repositories.auth_repository import AuthRepository
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import AuthCreate
from app.schemas.user_schema import UserCreate, UserRole, UserRole
from app.core.exceptions import UnprocessableEntityError, ForbiddenError


class UserService:
    def __init__(self, repo: UserRepository, auth: AuthRepository):
        self.repo = repo
        self.auth = auth

    async def create_user(self, user: UserCreate):
        existing = await self.repo.get_user_by_email(user.email)
        if existing:
            raise ValueError("Email already exists")
        userCreated = await self.repo.create_user(user)

        hashed_password = hash_password(user.password)
        auth_data = AuthCreate(
            user_id=userCreated.id,
            hashed_password=hashed_password
        )
        await self.auth.create_auth(auth_data)
        return userCreated

    async def list_users(self):
        return await self.repo.get_users()
    
    async def list_users_by_role(self, role: str):
        if role not in UserRole:
            raise UnprocessableEntityError("Invalid role value")
        return await self.repo.get_users_by_role(role)
    
    async def get_user_by_email(self, email: str):
        return await self.repo.get_user_by_email(email)