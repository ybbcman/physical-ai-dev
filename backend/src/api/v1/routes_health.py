from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

from backend.src.common.response import ApiResponse


router = APIRouter()


@router.get("/health", response_model = ApiResponse[dict], summary="API서버의 동작유무를 체크", description="API 서버의 서버에 대한 응답성을 체크합니다")
async def health_check():
    return ApiResponse(
        data = {"status": "ok"}
    )