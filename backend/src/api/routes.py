from fastapi import APIRouter, status
from fastapi.responses import PlainTextResponse, Response

home_router = APIRouter()


@home_router.get("/", response_description="Homepage", include_in_schema=False)
def home() -> Response:
    return PlainTextResponse("127.0.0.1", status_code=status.HTTP_200_OK)
