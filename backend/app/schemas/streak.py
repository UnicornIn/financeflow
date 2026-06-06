from pydantic import BaseModel
from datetime import datetime


class StreakOut(BaseModel):
    user_id: str
    current: int
    longest: int
    last_updated: datetime
    
    class Config:
        from_attributes = True


class LeaderboardEntry(BaseModel):
    user_id: str
    user_name: str
    current_streak: int
    longest_streak: int
    rank: int
