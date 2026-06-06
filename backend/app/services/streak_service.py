from typing import Optional, List
from app.repositories.streak_repository import StreakRepository
from app.repositories.user_repository import UserRepository
from app.models.streak import Streak


class StreakService:
    @staticmethod
    async def get_current_streak(user_id: str) -> Optional[Streak]:
        streak = await StreakRepository.get_current(user_id)
        if not streak:
            streak = await StreakRepository.create_or_get(user_id)
        return streak

    @staticmethod
    async def increment_streak(user_id: str) -> Streak:
        return await StreakRepository.increment(user_id)

    @staticmethod
    async def get_leaderboard(limit: int = 10) -> List[dict]:
        streaks = await StreakRepository.get_leaderboard(limit)
        leaderboard = []
        for user_id, current, longest in streaks:
            user = await UserRepository.get(user_id)
            if user:
                leaderboard.append({
                    "user_id": user_id,
                    "user_name": user.full_name or user.email.split("@")[0],
                    "current_streak": current,
                    "longest_streak": longest,
                    "rank": len(leaderboard) + 1
                })
        return leaderboard
