from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware
from util.logging_utils import logger, get_extra_info
from routing.public_router import public_router


app = FastAPI()
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
    root_path: str = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + str(app.openapi_url)
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
