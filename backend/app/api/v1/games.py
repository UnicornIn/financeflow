from fastapi import APIRouter, HTTPException, Header
from typing import Optional, List
from app.services.game_service import GameService
from app.services.auth_service import AuthService
from app.schemas.game import ScenarioOut, ScenarioDetail, GameResponse

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/scenarios", response_model=List[ScenarioOut])
async def get_scenarios(limit: int = 10):
    scenarios = await GameService.list_scenarios(limit)
    return scenarios


@router.get("/scenarios/{id}", response_model=ScenarioDetail)
async def get_scenario(id: str):
    scenario = await GameService.get_scenario(id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scenario


@router.post("/responses")
async def post_response(data: GameResponse, authorization: Optional[str] = Header(None)):
    # Verify token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    user_id = AuthService.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:
        result = await GameService.check_answer(data.scenario_id, data.user_answer)
        if result["is_correct"]:
            # Increment streak on correct answer
            from app.services.streak_service import StreakService
            await StreakService.increment_streak(user_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
