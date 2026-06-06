from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class MessageCreate(BaseModel):
    text: str


class MessageOut(BaseModel):
    id: str
    sender_id: str
    text: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class ChatCreate(BaseModel):
    title: Optional[str] = None


class ChatMessageCreate(BaseModel):
    title: Optional[str] = None
    text: str


class ChatOut(BaseModel):
    id: str
    user_id: str
    title: Optional[str]
    messages: List[MessageOut]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
