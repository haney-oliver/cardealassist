from fastapi import APIRouter
from model.service_healthcheck import HealthcheckResponse


public_router = APIRouter(prefix="/public")


# Example open service
@public_router.get("/v1/healthz", response_model=HealthcheckResponse)
def healthcheck():
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": "Service healthy!", "ok": True}
