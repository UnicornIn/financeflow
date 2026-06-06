from typing import Optional, List
from app.models.concept import Concept

# In-memory store with sample concepts
concepts_db = {
    "1": Concept(
        id="1",
        title="What is Budgeting?",
        description="Learn the basics of budgeting",
        content="Budgeting is the process of creating a plan to spend your money...",
        category="budgeting",
        difficulty="beginner"
    ),
    "2": Concept(
        id="2",
        title="Credit Score Basics",
        description="Understanding your credit score",
        content="Your credit score is a three-digit number that represents your creditworthiness...",
        category="credit",
        difficulty="beginner"
    ),
    "3": Concept(
        id="3",
        title="Investment Strategies",
        description="Different investment approaches",
        content="There are many investment strategies from conservative to aggressive...",
        category="investing",
        difficulty="advanced"
    ),
}


class ConceptRepository:
    @staticmethod
    async def list_all(limit: int = 50) -> List[Concept]:
        return list(concepts_db.values())[:limit]

    @staticmethod
    async def get(concept_id: str) -> Optional[Concept]:
        return concepts_db.get(concept_id)

    @staticmethod
    async def get_by_category(category: str) -> List[Concept]:
        return [c for c in concepts_db.values() if c.category == category]

    @staticmethod
    async def search(query: str) -> List[Concept]:
        query_lower = query.lower()
        return [
            c for c in concepts_db.values()
            if query_lower in c.title.lower() or query_lower in c.description.lower()
        ]
