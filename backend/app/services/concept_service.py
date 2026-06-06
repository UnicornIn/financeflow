from typing import Optional, List
from app.repositories.concept_repository import ConceptRepository
from app.models.concept import Concept


class ConceptService:
    @staticmethod
    async def list_concepts(limit: int = 50) -> List[Concept]:
        return await ConceptRepository.list_all(limit)

    @staticmethod
    async def get_concept(concept_id: str) -> Optional[Concept]:
        return await ConceptRepository.get(concept_id)

    @staticmethod
    async def get_by_category(category: str) -> List[Concept]:
        return await ConceptRepository.get_by_category(category)

    @staticmethod
    async def search_concepts(query: str) -> List[Concept]:
        return await ConceptRepository.search(query)
