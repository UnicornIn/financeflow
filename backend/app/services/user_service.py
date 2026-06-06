from typing import Optional
from app.repositories.user_repository import UserRepository
from app.models.user import User


class UserService:
    @staticmethod
    async def get_user(user_id: str) -> Optional[User]:
        return await UserRepository.get(user_id)

    @staticmethod
    async def update_user(user_id: str, full_name: Optional[str] = None, email: Optional[str] = None) -> Optional[User]:
        updates = {}
        if full_name is not None:
            updates["full_name"] = full_name
        if email is not None:
            updates["email"] = email
        return await UserRepository.update(user_id, **updates)

    @staticmethod
    async def delete_user(user_id: str) -> bool:
        return await UserRepository.delete(user_id)
