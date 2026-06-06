from typing import Optional, Tuple
from datetime import datetime, timedelta
import hashlib
import secrets
from app.repositories.user_repository import UserRepository
from app.models.user import User

# Simple in-memory token store
tokens_db = {}  # {token: (user_id, expiry)}


class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        """Simple password hashing (use bcrypt in production)."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        return AuthService.hash_password(password) == hashed

    @staticmethod
    def generate_token(user_id: str) -> str:
        """Generate a simple token."""
        token = secrets.token_urlsafe(32)
        expiry = datetime.utcnow() + timedelta(days=7)
        tokens_db[token] = (user_id, expiry)
        return token

    @staticmethod
    def verify_token(token: str) -> Optional[str]:
        """Verify token and return user_id if valid."""
        if token in tokens_db:
            user_id, expiry = tokens_db[token]
            if datetime.utcnow() < expiry:
                return user_id
            else:
                del tokens_db[token]
        return None

    @staticmethod
    async def register(email: str, password: str, full_name: Optional[str] = None) -> Tuple[User, str]:
        """Register a new user."""
        existing = await UserRepository.get_by_email(email)
        if existing:
            raise ValueError("Email already registered")
        
        hashed_pwd = AuthService.hash_password(password)
        user = await UserRepository.create(email, hashed_pwd, full_name)
        token = AuthService.generate_token(user.id)
        return user, token

    @staticmethod
    async def login(email: str, password: str) -> Tuple[User, str]:
        """Authenticate user and return token."""
        user = await UserRepository.get_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")
        
        if not AuthService.verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")
        
        token = AuthService.generate_token(user.id)
        return user, token

    @staticmethod
    async def refresh_token(token: str) -> Optional[str]:
        """Generate a new token from an existing valid token."""
        user_id = AuthService.verify_token(token)
        if user_id:
            # Invalidate old token
            if token in tokens_db:
                del tokens_db[token]
            return AuthService.generate_token(user_id)
        return None
