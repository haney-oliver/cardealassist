from fastapi import APIRouter
from pymongo.collection import Collection
from pymongo.database import Database
from model.service_healthcheck import HealthcheckResponse
from model.appraisal import AppraisalRequest, AppraisalResponse
from model.cars import (
    GetCarRequest,
    GetCarResponse,
    PaginationRequest,
    ListCarsResponse,
)
from fastapi.security import OAuth2PasswordBearer
from logic import cars
from logic import appraisal
import logic.user
from model.user import (
    LoginRequest,
    LoginResponse,
    RegistrationRequest,
    RegistrationResponse,
    User,
)
from db.db import DatabaseClient
from util.logging_utils import logger

public_router = APIRouter(prefix="/public")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db_client = DatabaseClient()
db = db_client.fetch_database("api-cardealassist")
user_collection: Collection = db.get_collection("users")

@public_router.get("/v1/healthz", response_model=HealthcheckResponse, tags=["Utility"])
def healthcheck():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}


@public_router.post("/v1/user/register", response_model=RegistrationResponse, tags=["Users"])
def register_user(user: User):
    return logic.user.register_user(user, user_collection)


@public_router.post("/v1/user/login", response_model=LoginResponse, tags=["Users"])
def login(req: LoginRequest):
    return logic.user.login_user(req, user_collection)

@public_router.post("/v1/cars/list", response_model=ListCarsResponse, tags=["Cars"])
async def list_cars(req: PaginationRequest):
    return await cars.list_cars(req, db["cardata"])


@public_router.post("/v1/cars/appraise", response_model=AppraisalResponse, tags=["Cars"])
async def appraise(req: AppraisalRequest):
    return await appraisal.get_appraisal(req)
