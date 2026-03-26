from fastapi import APIRouter, Depends, HTTPException
from app.core.auth import get_current_user
from app.schemas.user_schema import UserCreate, UserResponse, UserRole
from app.services.user_service import UserService
from app.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
):
    user =  await service.create_user(user)
    return user

@router.get("/", response_model=list[UserResponse])
async def get_users(
    role: int | None = None,
    service: UserService = Depends(get_user_service),
    current_user: str = Depends(get_current_user)
):
    if role is not None:
        return await service.list_users_by_role(role)
    return await service.list_users()