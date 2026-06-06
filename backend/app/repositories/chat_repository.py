from datetime import datetime
from typing import Optional, List
from uuid import uuid4
from pymongo import ReturnDocument
from app.database.mongodb import get_database
from app.models.chat import Chat, Message


def _doc_to_message(doc: dict) -> Message:
    return Message(
        id=doc["id"],
        sender_id=doc["sender_id"],
        text=doc["text"],
        created_at=doc["created_at"],
    )


def _doc_to_chat(doc: dict) -> Chat:
    return Chat(
        id=str(doc["_id"]),
        user_id=doc["user_id"],
        title=doc.get("title"),
        messages=[_doc_to_message(message) for message in doc.get("messages", [])],
        created_at=doc["created_at"],
        updated_at=doc["updated_at"],
    )


class ChatRepository:
    @staticmethod
    async def create(user_id: str, title: Optional[str] = None) -> Chat:
        chat_id = str(uuid4())
        now = datetime.utcnow()
        document = {
            "_id": chat_id,
            "user_id": user_id,
            "title": title,
            "messages": [],
            "created_at": now,
            "updated_at": now,
        }
        await get_database()["chats"].insert_one(document)
        return _doc_to_chat(document)

    @staticmethod
    async def get(chat_id: str) -> Optional[Chat]:
        document = await get_database()["chats"].find_one({"_id": chat_id})
        return _doc_to_chat(document) if document else None

    @staticmethod
    async def get_by_user(user_id: str) -> List[Chat]:
        cursor = get_database()["chats"].find({"user_id": user_id}).sort("updated_at", -1)
        documents = await cursor.to_list(length=50)
        return [_doc_to_chat(document) for document in documents]

    @staticmethod
    async def save_message(chat_id: str, sender_id: str, text: str) -> Message:
        msg_id = str(uuid4())
        now = datetime.utcnow()
        message = {
            "id": msg_id,
            "sender_id": sender_id,
            "text": text,
            "created_at": now,
        }
        document = await get_database()["chats"].find_one_and_update(
            {"_id": chat_id},
            {
                "$push": {"messages": message},
                "$set": {"updated_at": now},
            },
            return_document=ReturnDocument.AFTER,
        )
        if not document:
            raise ValueError(f"Chat {chat_id} not found")
        return _doc_to_message(message)

    @staticmethod
    async def delete(chat_id: str) -> bool:
        result = await get_database()["chats"].delete_one({"_id": chat_id})
        return result.deleted_count == 1
