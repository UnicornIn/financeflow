from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_perfil():
    """Obtiene el perfil del usuario"""
    return {"mensaje": "Perfil endpoint"}

@router.put("/")
async def update_perfil(data: dict):
    """Actualiza el perfil del usuario"""
    return {"actualizado": data}
