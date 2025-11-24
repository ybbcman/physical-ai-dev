from fastapi import APIRouter
from backend.src.common.response import ApiResponse
from backend.src.core.config import settings

router = APIRouter()

@router.get("/info", response_model = ApiResponse[dict], summary="서비스 정보 조회", description="현재 API 서버의 기본정보를 반환합니다")
async def get_service_info():
    return ApiResponse(
        data = {
            "name": settings.app_name,
            "version": settings.app_version,
        }
    )
