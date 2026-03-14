from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_chat():
    """Obtiene el chat"""
    return {"mensaje": "Chat endpoint"}

@router.post("/mensaje")
async def send_message(message: str):
    """Envía un mensaje al chat"""
    return {"respuesta": message}
