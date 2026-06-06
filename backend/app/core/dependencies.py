from fastapi import Depends, HTTPException


def get_current_user(token: str = None):
    # Placeholder dependency for current user
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"user_id": "anonymous"}
