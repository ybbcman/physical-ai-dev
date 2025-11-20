from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response


router = APIRouter()


@router.get("/health", summary="Health Check")
async def health_check():
    return JSONResponse({"status": "ok"})
