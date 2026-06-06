"""Concept DB model."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Concept:
    id: str
    title: str
    description: str = ""
    content: Optional[str] = None
    category: Optional[str] = None  # budgeting, investing, savings, credit
    difficulty: str = "beginner"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
