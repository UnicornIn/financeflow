from typing import Optional, List
from app.repositories.chat_repository import ChatRepository
from app.models.chat import Chat, Message


class ChatService:
    @staticmethod
    async def create_chat(user_id: str, title: Optional[str] = None) -> Chat:
        return await ChatRepository.create(user_id, title)

    @staticmethod
    async def get_chat_history(chat_id: str) -> Optional[Chat]:
        return await ChatRepository.get(chat_id)

    @staticmethod
    async def get_user_chats(user_id: str) -> List[Chat]:
        return await ChatRepository.get_by_user(user_id)

    @staticmethod
    async def send_message(chat_id: str, sender_id: str, text: str) -> Message:
        return await ChatRepository.save_message(chat_id, sender_id, text)

    @staticmethod
    async def delete_chat(chat_id: str) -> bool:
        return await ChatRepository.delete(chat_id)
