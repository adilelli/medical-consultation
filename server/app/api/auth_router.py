from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import create_access_token, verify_password
from app.dependencies import get_auth_service, get_user_service
from app.schemas.auth_schema import LoginRequest
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login( login_request: LoginRequest, service: AuthService = Depends(get_auth_service)):
    # TODO: fetch user from DB
    auth = await service.validate_auth(login_request.email, login_request.password)

    access_token = create_access_token({"sub": str(auth.id)})
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,  # Prevents JS access (security)
        secure=False,    # HTTPS only
        samesite='lax',
        max_age=3600    # 1 hour
    )
    return response
