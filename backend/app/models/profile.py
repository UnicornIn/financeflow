"""Profile DB model."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Profile:
    user_id: str
    display_name: str = ""
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    financial_profile: Optional[str] = None  # conservative, moderate, aggressive
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
