from model.base import Base
from typing import Optional


class User(Base):
    first_name: str
    last_name: str
    email_address: str
    phone_number: str
    street_address: str
    external_id: str
    city: str
    zip_code: str
    state: str


class RegistrationRequest(Base):
    user: User


class RegistrationResponse(Base):
    success: bool
    message: str


class LoginRequest(Base):
    external_id: str


class LoginResponse(Base):
    user: Optional[User] = None
    message: str
