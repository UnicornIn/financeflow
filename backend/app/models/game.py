"""Game/Scenario DB model."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Scenario:
    id: str
    title: str
    description: str
    situation: str
    options: list  # List of options for user to choose
    correct_answer: int
    explanation: str
    difficulty: str = "medium"  # easy, medium, hard
    created_at: datetime = field(default_factory=datetime.utcnow)
