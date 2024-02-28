from pymongo.collection import Collection
from pymongo.results import InsertOneResult
from model.user import (
    LoginRequest,
    RegistrationResponse,
    LoginResponse,
    User,
)
from util.logging_utils import logger

def register_user(user: User, collection: Collection) -> RegistrationResponse:
    result: InsertOneResult = collection.insert_one(document=user.model_dump())
    if result.inserted_id:
        return RegistrationResponse(success=True, message="User created successfully!")
    else:
        return RegistrationResponse(success=False, message="Failed to create user.")


def login_user(req: LoginRequest, collection: Collection) -> LoginResponse:
    result = collection.find_one({"external_id": req.external_id})
    if result:
        logger.info(User(**result))
        return LoginResponse(user=User(**result), message="Login successful!")
    else:
        return LoginResponse(message="Failed to login.")
