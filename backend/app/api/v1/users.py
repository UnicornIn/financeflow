from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.schemas.user import UserOut, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


def get_user_id_from_token(authorization: Optional[str]):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    user_id = AuthService.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id


@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    user = await UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: str, data: UserUpdate, authorization: Optional[str] = Header(None)):
    # Verify token and ownership
    current_user_id = get_user_id_from_token(authorization)
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    user = await UserService.update_user(user_id, full_name=data.full_name, email=data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: str, authorization: Optional[str] = Header(None)):
    # Verify token and ownership
    current_user_id = get_user_id_from_token(authorization)
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    success = await UserService.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
