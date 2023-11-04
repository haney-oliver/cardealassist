from fastapi import APIRouter
from model.service_healthcheck import HealthcheckResponse
from model.cars import GetCarRequest, GetCarResponse, ListCarsRequest, ListCarsResponse
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from starlette.config import Config
from logic import cars
from db.db import DatabaseClient

public_router = APIRouter(prefix="/public")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db_client = DatabaseClient()
db = db_client.fetch_database("api-cardealassist")

@public_router.get("/v1/healthz", response_model=HealthcheckResponse)
def healthcheck():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}


@public_router.get("/v1/register", response_model=HealthcheckResponse)
def register():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}


@public_router.get("/v1/login", response_model=HealthcheckResponse)
def login():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}


@public_router.post("/v1/cars/list", response_model=ListCarsResponse)
async def list_cars(req: ListCarsRequest):
    return await cars.list_cars(req, db["cardata"])

@public_router.post("/v1/cars/get", response_model=GetCarResponse)
async def list_cars(req: GetCarRequest):
    return await cars.get_car(req, db["cardata"])
