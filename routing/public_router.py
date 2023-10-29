from fastapi import APIRouter
from model.service_healthcheck import HealthcheckResponse
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from starlette.config import Config

public_router = APIRouter(prefix="/public")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@public_router.get("/v1/healthz", response_model=HealthcheckResponse)
def healthcheck():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}


@public_router.get("/v1/register", response_model=HealthcheckResponse)
def healthcheck():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}


@public_router.get("/v1/login", response_model=HealthcheckResponse)
def healthcheck():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}
