from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from app.services.auth_service import AuthService
from app.schemas.auth import UserRegister, UserLogin, Token, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=Token)
async def register(data: UserRegister):
    try:
        user, token = await AuthService.register(data.email, data.password, data.full_name)
        return {"access_token": token, "token_type": "bearer", "user_id": user.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=Token)
async def login(data: UserLogin):
    try:
        user, token = await AuthService.login(data.email, data.password)
        return {"access_token": token, "token_type": "bearer", "user_id": user.id}
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/me", response_model=UserResponse)
async def get_me(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    
    token = authorization.replace("Bearer ", "")
    user_id = AuthService.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    from app.services.user_service import UserService
    user = await UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active
    }


@router.post("/refresh-token", response_model=Token)
async def refresh_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    
    token = authorization.replace("Bearer ", "")
    new_token = await AuthService.refresh_token(token)
    if not new_token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = AuthService.verify_token(new_token)
    return {"access_token": new_token, "token_type": "bearer", "user_id": user_id}
