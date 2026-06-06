from typing import Optional
from app.repositories.profile_repository import ProfileRepository
from app.repositories.user_repository import UserRepository
from app.models.profile import Profile


class ProfileService:
    @staticmethod
    async def get_profile(user_id: str) -> Optional[Profile]:
        profile = await ProfileRepository.get_by_user(user_id)
        if not profile:
            # Create default profile if doesn't exist
            user = await UserRepository.get(user_id)
            if user:
                profile = await ProfileRepository.create_or_update(
                    user_id,
                    display_name=user.full_name or user.email.split("@")[0]
                )
        return profile

    @staticmethod
    async def update_profile(user_id: str, **kwargs) -> Optional[Profile]:
        return await ProfileRepository.update(user_id, **kwargs)

    @staticmethod
    async def submit_quiz(user_id: str, answers: dict) -> dict:
        """Process quiz submission and update profile."""
        # Analyze answers to determine financial profile
        # This is a simplified version
        profile = await ProfileService.get_profile(user_id)
        if profile:
            # Determine profile type based on answers
            profile.financial_profile = "moderate"  # Simplified
            await ProfileRepository.update(user_id, financial_profile=profile.financial_profile)
        return {"quiz_completed": True, "profile_type": profile.financial_profile if profile else None}
