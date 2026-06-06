from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from app.services.profile_service import ProfileService
from app.services.auth_service import AuthService
from app.schemas.profile import ProfileOut, ProfileUpdate, QuizSubmit

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/{user_id}", response_model=ProfileOut)
async def get_profile(user_id: str):
    profile = await ProfileService.get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.post("/quiz/submit")
async def submit_quiz(data: QuizSubmit, authorization: Optional[str] = Header(None)):
    # Verify token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    user_id = AuthService.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    result = await ProfileService.submit_quiz(user_id, data.answers)
    return result


@router.put("/{user_id}", response_model=ProfileOut)
async def update_profile(user_id: str, data: ProfileUpdate, authorization: Optional[str] = Header(None)):
    # Verify token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    current_user_id = AuthService.verify_token(token)
    if not current_user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    profile = await ProfileService.update_profile(user_id, **data.dict(exclude_unset=True))
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
