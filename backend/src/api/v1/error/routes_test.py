from fastapi import APIRouter
from backend.src.common.exceptions import BeException

router = APIRouter()

@router.get("/error/test")
async def test_error():
    raise BeException("Test error occurred forcely", status_code = 400)