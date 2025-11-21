from fastapi import APIRouter
from . import routes_health, routes_info, routes_echo

api_router = APIRouter()
api_router.include_router(routes_health.router, prefix="", tags=["health"])
api_router.include_router(routes_info.router, prefix="", tags=["info"])
api_router.include_router(routes_echo.router, prefix="", tags=["echo"])