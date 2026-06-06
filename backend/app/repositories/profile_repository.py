from datetime import datetime
from typing import Optional
from pymongo import ReturnDocument
from app.database.mongodb import get_database
from app.models.profile import Profile


def _doc_to_profile(doc: dict) -> Profile:
    return Profile(
        user_id=doc["user_id"],
        display_name=doc.get("display_name"),
        bio=doc.get("bio"),
        financial_profile=doc.get("financial_profile"),
        created_at=doc["created_at"],
        updated_at=doc["updated_at"],
    )


class ProfileRepository:
    @staticmethod
    async def get_by_user(user_id: str) -> Optional[Profile]:
        document = await get_database()["profiles"].find_one({"user_id": user_id})
        return _doc_to_profile(document) if document else None

    @staticmethod
    async def create_or_update(user_id: str, **kwargs) -> Profile:
        now = datetime.utcnow()
        updates = {key: value for key, value in kwargs.items() if value is not None}
        updates["updated_at"] = now
        document = await get_database()["profiles"].find_one_and_update(
            {"user_id": user_id},
            {
                "$set": updates,
                "$setOnInsert": {"user_id": user_id, "created_at": now},
            },
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )
        return _doc_to_profile(document)

    @staticmethod
    async def update(user_id: str, **kwargs) -> Optional[Profile]:
        now = datetime.utcnow()
        updates = {key: value for key, value in kwargs.items() if value is not None}
        if not updates:
            return await ProfileRepository.get_by_user(user_id)

        updates["updated_at"] = now
        document = await get_database()["profiles"].find_one_and_update(
            {"user_id": user_id},
            {"$set": updates},
            return_document=ReturnDocument.AFTER,
        )
        return _doc_to_profile(document) if document else None
