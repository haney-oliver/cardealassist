from pydantic import BaseModel
from typing import Optional


class SellerDTO(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    name: Optional[str] = None
    website: Optional[str] = None


class CarDTO(BaseModel):
    details_path: Optional[str] = None
    drivetrain: Optional[str] = None
    exterior: Optional[str] = None
    fuel_type: Optional[str] = None
    interior: Optional[str] = None
    mileage: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    vin: Optional[str] = None
    seller: SellerDTO


class Response(BaseModel):
    ok: bool
    message: str


class ListCarsRequest(BaseModel):
    page: int
    size: int
    filter: Optional[dict[str, str]] = None


class GetCarRequest(BaseModel):
    vin: Optional[str] = None
    id: Optional[str] = None


class GetCarResponse(Response):
    car: Optional[CarDTO] = None


class ListCarsResponse(Response):
    cars: list[CarDTO] = None
