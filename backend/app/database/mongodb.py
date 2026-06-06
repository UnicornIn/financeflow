"""MongoDB connection helpers for the FinanceFlow backend."""

from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

mongodb_client: Optional[AsyncIOMotorClient] = None
mongodb_db: Optional[AsyncIOMotorDatabase] = None


async def init_db(uri: str) -> None:
    global mongodb_client, mongodb_db
    mongodb_client = AsyncIOMotorClient(uri)
    mongodb_db = mongodb_client["financeflow"]

    # Ensure indexes for faster lookups and unique constraints.
    await mongodb_db["users"].create_index("email", unique=True)
    await mongodb_db["profiles"].create_index("user_id", unique=True)
    await mongodb_db["streaks"].create_index("user_id", unique=True)
    await mongodb_db["chats"].create_index("user_id")


def get_database() -> AsyncIOMotorDatabase:
    if mongodb_db is None:
        raise RuntimeError("MongoDB is not initialized. Call init_db first.")
    return mongodb_db


def close_db() -> None:
    if mongodb_client is not None:
        mongodb_client.close()
