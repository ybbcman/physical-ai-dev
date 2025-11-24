from fastapi import APIRouter
from pydantic import BaseModel

from backend.src.common.response import ApiResponse

router = APIRouter()

class EchoRequest(BaseModel):
    message: str
    user: str | None = None

class EchoResponse(BaseModel):
    message: str
    user: str | None = None
    length: int

@router.post("/echo", response_model = ApiResponse[EchoResponse], summary="Echo back your message", description="사용자가 보낸 메세지를 다시 회신합니다")
async def echo(request: EchoRequest):
    return ApiResponse(
        data = EchoResponse(
            message = request.message,
            user = request.user,
            length = len(request.message)
        )
    )