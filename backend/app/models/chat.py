"""Chat DB model."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Message:
    id: str
    sender_id: str
    text: str
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Chat:
    id: str
    user_id: str
    messages: List[Message] = field(default_factory=list)
    title: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
