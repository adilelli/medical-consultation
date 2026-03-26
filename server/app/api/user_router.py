from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import UserService
from app.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return await service.create_user(user)

@router.get("/", response_model=list[UserResponse])
async def get_users(
    role: str | None = None,
    service: UserService = Depends(get_user_service)
):
    if role:
        return await service.list_users_by_role(role)
    return await service.list_users()