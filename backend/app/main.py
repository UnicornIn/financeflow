"""Main entrypoint for the backend FastAPI application.

Registers API routers and manages lifecycle events (db init/close).
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database.mongodb import init_db, close_db
from app.api.v1 import auth, users, profiles, streaks, chat, games, concepts


app = FastAPI(title="FinanceFlow Backend")

# Minimal CORS (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await init_db(settings.mongodb_uri)


@app.on_event("shutdown")
async def shutdown_event():
    close_db()


api_v1_prefix = "/api/v1"
app.include_router(auth.router, prefix=api_v1_prefix)
app.include_router(users.router, prefix=api_v1_prefix)
app.include_router(profiles.router, prefix=api_v1_prefix)
app.include_router(streaks.router, prefix=api_v1_prefix)
app.include_router(chat.router, prefix=api_v1_prefix)
app.include_router(games.router, prefix=api_v1_prefix)
app.include_router(concepts.router, prefix=api_v1_prefix)


@app.get("/")
async def read_root():
    return {"message": f"{settings.app_name} backend is running"}
