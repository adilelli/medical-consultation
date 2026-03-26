from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user_schema import UserCreate, UserResponse, UserRole
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
    role: int | None = None,
    service: UserService = Depends(get_user_service)
):
    if role is not None:
        if role not in UserRole:
            raise HTTPException(status_code=422, detail="Invalid role value")
        return await service.list_users_by_role(role)
    return await service.list_users()