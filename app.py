from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html

from util.logging_utils import logger, get_extra_info

from routing.admin_router import admin_router
from routing.public_router import public_router

# Connect to a db using sqlalchemy
# engine = db.create_engine("mysql+pymysql://root@localhost:3306/example")

app = FastAPI()
app.include_router(admin_router)
app.include_router(public_router)


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
        extra={"extra_info": get_extra_info(request, response)},
    )
    return response
