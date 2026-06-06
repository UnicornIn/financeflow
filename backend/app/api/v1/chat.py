from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from app.services.chat_service import ChatService
from app.services.auth_service import AuthService
from app.schemas.chat import ChatOut, ChatMessageCreate

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/message")
async def post_message(data: ChatMessageCreate, authorization: Optional[str] = Header(None)):
    # Verify token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    user_id = AuthService.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Create chat if doesn't exist
    chat = await ChatService.create_chat(user_id, data.title)
    
    # Save message
    message = await ChatService.send_message(chat.id, user_id, data.text)
    return {
        "chat_id": chat.id,
        "message_id": message.id,
        "created_at": message.created_at
    }


@router.get("/{conversation_id}/history", response_model=ChatOut)
async def get_chat_history(conversation_id: str, authorization: Optional[str] = Header(None)):
    # Verify token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    user_id = AuthService.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    chat = await ChatService.get_chat_history(conversation_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    # Verify ownership
    if chat.user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    return chat


@router.delete("/{conversation_id}")
async def delete_chat(conversation_id: str, authorization: Optional[str] = Header(None)):
    # Verify token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = authorization.replace("Bearer ", "")
    user_id = AuthService.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    chat = await ChatService.get_chat_history(conversation_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    # Verify ownership
    if chat.user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    success = await ChatService.delete_chat(conversation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Chat not found")
    return {"detail": "Chat deleted successfully"}
