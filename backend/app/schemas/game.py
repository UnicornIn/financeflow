from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ScenarioOut(BaseModel):
    id: str
    title: str
    description: str
    situation: str
    options: List[str]
    difficulty: str
    
    class Config:
        from_attributes = True


class ScenarioDetail(ScenarioOut):
    explanation: str
    correct_answer: int


class GameResponse(BaseModel):
    scenario_id: str
    user_answer: int
    is_correct: bool
