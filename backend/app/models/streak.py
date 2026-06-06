"""Streak DB model."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Streak:
    user_id: str
    current: int = 0
    longest: int = 0
    last_updated: datetime = field(default_factory=datetime.utcnow)
    created_at: datetime = field(default_factory=datetime.utcnow)
