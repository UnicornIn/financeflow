from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ConceptBase(BaseModel):
    title: str
    description: str = ""
    content: Optional[str] = None
    category: Optional[str] = None
    difficulty: str = "beginner"


class ConceptOut(ConceptBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ConceptSearch(BaseModel):
    query: str
