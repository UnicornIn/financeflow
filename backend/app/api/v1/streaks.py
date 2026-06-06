from fastapi import APIRouter, HTTPException, Header
from typing import Optional, List
from app.services.streak_service import StreakService
from app.services.auth_service import AuthService
from app.schemas.streak import StreakOut, LeaderboardEntry

router = APIRouter(prefix="/streaks", tags=["streaks"])


@router.get("/{user_id}", response_model=StreakOut)
async def get_streak(user_id: str):
    streak = await StreakService.get_current_streak(user_id)
    if not streak:
        raise HTTPException(status_code=404, detail="Streak not found")
    return streak


@router.post("/{user_id}/increment", response_model=StreakOut)
async def increment_streak(user_id: str, authorization: Optional[str] = Header(None)):
    # Verify token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    current_user_id = AuthService.verify_token(token)
    if not current_user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    streak = await StreakService.increment_streak(user_id)
    return streak


@router.get("/leaderboard/top", response_model=List[LeaderboardEntry])
async def get_leaderboard(limit: int = 10):
    leaderboard = await StreakService.get_leaderboard(limit)
    return leaderboard
