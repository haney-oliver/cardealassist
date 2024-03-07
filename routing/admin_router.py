from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from util.logging_utils import logger
from model.service_admin_example import AdminRequest, AdminResponse
import jwt


admin_router = APIRouter(prefix="/admin")

# Define an API key
SECRET_KEY = "<YOUR_API_KEY>"


# Define a function that checks the API key
def check_api_key(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
):
    # If no API key is provided, return an error
    token = credentials.credentials
    logger.info("token: {}".format(token))
    if token is None:
        raise HTTPException(
            status_code=401, detail="Please provide an API key"
        )

    # Decode the JWT token using the secret key
    try:
        _ = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.DecodeError as e:
        logger.error(e)
        raise HTTPException(status_code=401, detail="Invalid API key")

    # If the API key is valid, return it
    return token


@admin_router.post("/v1/example", response_model=AdminResponse)
def admin_example(
    request: AdminRequest, api_key: str = Depends(check_api_key)
):
    # Interperet request values
    message = str(request.flag)
    # Return response in shape of Response object defined with the above pydantic model
    return {"message": message}
