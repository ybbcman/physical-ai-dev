from fastapi import APIRouter
from backend.src.core.config import settings

router = APIRouter()

@router.get("/info", summary="Service Information")
async def get_service_info():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "description": "API Backend for my physical-ai portfolio project",
    }