from fastapi import APIRouter
from . import routes_health

api_router = APIRouter()
api_router.include_router(routes_health.router, prefix="", tags=["health"])