from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProfileBase(BaseModel):
    display_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    financial_profile: Optional[str] = None


class ProfileUpdate(ProfileBase):
    pass


class QuizSubmit(BaseModel):
    answers: dict  # {question_id: answer}


class ProfileOut(ProfileBase):
    user_id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
