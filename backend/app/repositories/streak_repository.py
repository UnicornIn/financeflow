from datetime import datetime
from typing import Optional, List, Tuple
from pymongo import ReturnDocument
from app.database.mongodb import get_database
from app.models.streak import Streak


def _doc_to_streak(doc: dict) -> Streak:
    return Streak(
        user_id=doc["user_id"],
        current=doc.get("current", 0),
        longest=doc.get("longest", 0),
        last_updated=doc["last_updated"],
        created_at=doc["created_at"],
    )


class StreakRepository:
    @staticmethod
    async def get_current(user_id: str) -> Optional[Streak]:
        document = await get_database()["streaks"].find_one({"user_id": user_id})
        return _doc_to_streak(document) if document else None

    @staticmethod
    async def create_or_get(user_id: str) -> Streak:
        now = datetime.utcnow()
        document = await get_database()["streaks"].find_one_and_update(
            {"user_id": user_id},
            {
                "$setOnInsert": {
                    "user_id": user_id,
                    "current": 0,
                    "longest": 0,
                    "last_updated": now,
                    "created_at": now,
                }
            },
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )
        return _doc_to_streak(document)

    @staticmethod
    async def increment(user_id: str) -> Streak:
        streak = await StreakRepository.create_or_get(user_id)
        streak.current += 1
        streak.longest = max(streak.longest, streak.current)
        streak.last_updated = datetime.utcnow()
        await get_database()["streaks"].update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "current": streak.current,
                    "longest": streak.longest,
                    "last_updated": streak.last_updated,
                }
            },
        )
        return streak

    @staticmethod
    async def reset(user_id: str) -> Streak:
        now = datetime.utcnow()
        document = await get_database()["streaks"].find_one_and_update(
            {"user_id": user_id},
            {"$set": {"current": 0, "last_updated": now}},
            return_document=ReturnDocument.AFTER,
        )
        return _doc_to_streak(document) if document else await StreakRepository.create_or_get(user_id)

    @staticmethod
    async def get_leaderboard(limit: int = 10) -> List[Tuple[str, int, int]]:
        cursor = get_database()["streaks"].find().sort("current", -1).limit(limit)
        documents = await cursor.to_list(length=limit)
        return [
            (doc["user_id"], doc.get("current", 0), doc.get("longest", 0))
            for doc in documents
        ]
