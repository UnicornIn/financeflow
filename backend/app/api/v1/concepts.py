from fastapi import APIRouter, HTTPException
from typing import List
from app.services.concept_service import ConceptService
from app.schemas.concept import ConceptOut, ConceptSearch

router = APIRouter(prefix="/concepts", tags=["concepts"])


@router.get("/", response_model=List[ConceptOut])
async def list_concepts(limit: int = 50):
    concepts = await ConceptService.list_concepts(limit)
    return concepts


@router.get("/{id}", response_model=ConceptOut)
async def get_concept(id: str):
    concept = await ConceptService.get_concept(id)
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    return concept


@router.get("/search")
async def search_concepts(q: str):
    if not q:
        raise HTTPException(status_code=400, detail="Query parameter 'q' is required")
    concepts = await ConceptService.search_concepts(q)
    return concepts


@router.get("/category/{cat}", response_model=List[ConceptOut])
async def get_by_category(cat: str):
    concepts = await ConceptService.get_by_category(cat)
    return concepts
