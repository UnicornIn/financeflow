from typing import Optional, List
from app.repositories.game_repository import GameRepository
from app.models.game import Scenario


class GameService:
    @staticmethod
    async def list_scenarios(limit: int = 10) -> List[Scenario]:
        return await GameRepository.list_scenarios(limit)

    @staticmethod
    async def get_scenario(scenario_id: str) -> Optional[Scenario]:
        return await GameRepository.get_scenario(scenario_id)

    @staticmethod
    async def check_answer(scenario_id: str, user_answer: int) -> dict:
        scenario = await GameRepository.get_scenario(scenario_id)
        if not scenario:
            raise ValueError("Scenario not found")
        
        is_correct = user_answer == scenario.correct_answer
        return {
            "is_correct": is_correct,
            "correct_answer": scenario.correct_answer,
            "explanation": scenario.explanation
        }
