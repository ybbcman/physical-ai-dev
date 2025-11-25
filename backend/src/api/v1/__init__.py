from fastapi import APIRouter
from . import routes_health, routes_info, routes_echo
from backend.src.api.v1.error import routes_test
from backend.src.db.models.user.routes import router as router_user

api_router = APIRouter()
api_router.include_router(routes_health.router, prefix="", tags=["health"])
api_router.include_router(routes_info.router, prefix="", tags=["info"])
api_router.include_router(routes_echo.router, prefix="", tags=["echo"])
api_router.include_router(routes_test.router, prefix="", tags=["test"])
api_router.include_router(router_user)