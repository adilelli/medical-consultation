from fastapi import HTTPException, Depends
from fastapi import security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import create_access_token, verify_password, hash_password, verify_token
from app.repositories.auth_repository import AuthRepository
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import AuthCreate
from app.schemas.user_schema import UserCreate
from app.core.exceptions import UnauthorizedError, ForbiddenError, BusinessLogicError

security = HTTPBearer()

class AuthService:
    def __init__(self, repo: AuthRepository, user: UserRepository):
        self.repo = repo
        self.user = user

    # async def create_auth(self, auth: AuthCreate, user: UserCreate):
    #     existing = await self.user.get_user_by_email(user.email)
    #     if existing:
    #         raise BusinessLogicError("Email already exists")
    #     auth.hashed_password = hash_password(auth.hashed_password)
    #     return await self.repo.create_auth(auth)

    async def validate_auth(self, email: str, password: str):
        user = await self.user.get_user_by_email(email)
        if not user:
            raise UnauthorizedError("User not found")
        auth = await self.repo.get_auth_by_id(user.id) if user else None
        if not auth:
            raise UnauthorizedError("Invalid password")
        if not verify_password(password, auth.hashed_password):
            raise UnauthorizedError("Invalid password")
        
        return user