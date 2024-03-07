from fastapi import APIRouter
from pymongo import collection
from pymongo.collection import Collection
from model.service_healthcheck import HealthcheckResponse
from model.appraisal import AppraisalRequest, AppraisalResponse
from model.cars import (
    PaginationRequest,
    ListCarsResponse,
)
from fastapi.security import OAuth2PasswordBearer
from logic import cars
from logic import appraisal
from logic import autovin
import logic.user
from model.user import (
    LoginRequest,
    LoginResponse,
    RegistrationResponse,
    User,
)
from db.db import DatabaseClient
from model.vin import VinInfo
from util.logging_utils import logger

public_router = APIRouter(prefix="/public")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db_client = DatabaseClient()
db = db_client.fetch_database("api-cardealassist")
user_collection: Collection = db.get_collection("users")
vin_collection: Collection = db.get_collection("vin")


@public_router.get(
    "/v1/healthz", response_model=HealthcheckResponse, tags=["Utility"]
)
def healthcheck():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}


@public_router.post(
    "/v1/user/register", response_model=RegistrationResponse, tags=["Users"]
)
def register_user(user: User):
    return logic.user.register_user(user, user_collection)


@public_router.post(
    "/v1/user/login", response_model=LoginResponse, tags=["Users"]
)
def login(req: LoginRequest):
    return logic.user.login_user(req, user_collection)


@public_router.get("/v1/autovin/get", response_model=VinInfo, tags=["Tools"])
def decode_vin(vin: str):
    vin_info: VinInfo | None = autovin.checkIfExists(vin_collection, vin)
    if not vin_info:
        vin_info = autovin.autovin(vin)
        autovin.saveVinData(vin_collection, vin_info, vin)
    return vin_info


@public_router.post(
    "/v1/cars/list", response_model=ListCarsResponse, tags=["Cars"]
)
async def list_cars(req: PaginationRequest):
    return await cars.list_cars(req, db["cardata"])


@public_router.post(
    "/v1/cars/appraise", response_model=AppraisalResponse, tags=["Cars"]
)
async def appraise(req: AppraisalRequest):
    return await appraisal.get_appraisal(req)
