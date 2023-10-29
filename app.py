from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from util.logging_utils import logger, get_extra_info
from pathlib import Path
from routing.admin_router import admin_router
from routing.public_router import public_router
from db.db import Database
from logic.cars import list_cars

# Connect to a db using sqlalchemy
# engine = db.create_engine("mysql+pymysql://root@localhost:3306/example")

app = FastAPI()
app.include_router(admin_router)
app.include_router(public_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="html")

db = Database()
db_session = db.get_session()


@app.get("/", include_in_schema=False)
async def home(req: Request):
    cars = await list_cars(req, db_session)
    return templates.TemplateResponse("public/home/homepage.html", {"request": req, "cars": cars})


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
