import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.src.api import routes
from backend.src.api.v1 import api_router
from backend.src.common.exceptions import BeException
from backend.src.common.response import ApiResponse
from backend.src.core.config import settings


logger = logging.getLogger(__name__)


tags_metadata = [
    {
        "name": "health",
        "description": "Health check for api",
    }
]

def create_app() -> FastAPI:
    app = FastAPI(
        title="physical-ai-dev",
        description="base project for fastapi backend",
        version=settings.api_version,
        openapi_url=f"/{settings.api_version}/openapi.json",
        openapi_tags=tags_metadata,
    )
    app.add_middleware(CORSMiddleware, allow_origins=["*"])
    app.add_event_handler("startup", on_startup)
    app.include_router(routes.home_router)
    app.include_router(api_router, prefix=f"/api/{settings.api_version}")

    return app

def on_startup() -> None:
    logger.info("FastAPI app running...")

app = create_app()

@app.exception_handler(BeException)
async def exception_handler(request: Request, exc: BeException):
    return JSONResponse(
        status_code = exc.status_code,
        content = ApiResponse(
            success = False,
            message = exc.message,
            data = None
        ).model_dump()
    )