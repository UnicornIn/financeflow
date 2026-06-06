from datetime import datetime
from typing import Optional
from uuid import uuid4
from pymongo import ReturnDocument
from app.database.mongodb import get_database
from app.models.user import User


def _doc_to_user(doc: dict) -> User:
    return User(
        id=str(doc["_id"]),
        email=doc["email"],
        hashed_password=doc["hashed_password"],
        full_name=doc.get("full_name"),
        is_active=doc.get("is_active", True),
        created_at=doc["created_at"],
        updated_at=doc["updated_at"],
    )


class UserRepository:
    @staticmethod
    async def create(email: str, hashed_password: str, full_name: Optional[str] = None) -> User:
        user_id = str(uuid4())
        now = datetime.utcnow()
        document = {
            "_id": user_id,
            "email": email,
            "hashed_password": hashed_password,
            "full_name": full_name,
            "is_active": True,
            "created_at": now,
            "updated_at": now,
        }
        await get_database()["users"].insert_one(document)
        return _doc_to_user(document)

    @staticmethod
    async def get(user_id: str) -> Optional[User]:
        document = await get_database()["users"].find_one({"_id": user_id})
        return _doc_to_user(document) if document else None

    @staticmethod
    async def get_by_email(email: str) -> Optional[User]:
        document = await get_database()["users"].find_one({"email": email})
        return _doc_to_user(document) if document else None

    @staticmethod
    async def update(user_id: str, **kwargs) -> Optional[User]:
        allowed_fields = {"email", "hashed_password", "full_name", "is_active"}
        now = datetime.utcnow()
        updates = {key: value for key, value in kwargs.items() if key in allowed_fields}
        if not updates:
            return await UserRepository.get(user_id)

        updates["updated_at"] = now
        document = await get_database()["users"].find_one_and_update(
            {"_id": user_id},
            {"$set": updates},
            return_document=ReturnDocument.AFTER,
        )
        return _doc_to_user(document) if document else None

    @staticmethod
    async def delete(user_id: str) -> bool:
        result = await get_database()["users"].delete_one({"_id": user_id})
        return result.deleted_count == 1
