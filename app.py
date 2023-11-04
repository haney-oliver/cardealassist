from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from util.logging_utils import logger, get_extra_info
from pathlib import Path
from routing.admin_router import admin_router
from routing.public_router import public_router
from db.db import DatabaseClient
from logic.cars import list_cars


app = FastAPI()
app.include_router(admin_router)
app.include_router(public_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title="API",
    )


@app.middleware("http")
async def log_request(request, call_next):
    response = await call_next(request)
    logger.info(
        request.method + " " + request.url.path,
        extra={"extra_info": get_extra_info(request)},
    )
    return response
