from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EchoRequest(BaseModel):
    message: str
    user: str | None = None

class EchoResponse(BaseModel):
    message: str
    user: str | None = None
    length: int

@router.post("/echo", response_model=EchoResponse, summary="Echo back your message")
async def echo(request: EchoRequest):
    return EchoResponse(
        message=request.message,
        user=request.user,
        length=len(request.message),
    )