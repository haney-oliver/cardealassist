from typing import Optional
from model.base import Base

class Features(Base):
    convenience: Optional[list[str]] = None
    entertainment: Optional[list[str]] = None
    exterior: Optional[list[str]] = None
    saftey: Optional[list[str]] = None
    seating: Optional[list[str]] = None


class SellerDTO(Base):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    name: Optional[str] = None
    website: Optional[str] = None
    rating: Optional[float] = None


class Rating(Base):
    comfort: Optional[float] = None
    interior: Optional[float] = None
    performance: Optional[float] = None
    value: Optional[float] = None
    exterior: Optional[float] = None
    reliability: Optional[float] = None


class CustomerReview(Base):
    rating: Optional[float] = None
    title: Optional[str] = None
    date: Optional[int] = None
    author: Optional[str] = None
    location: Optional[str] = None
    owner: Optional[bool] = None
    content: Optional[str] = None


class PriceChange(Base):
    date: Optional[int] = None
    change: Optional[float | str] = None
    price: Optional[float] = None


class CarDTO(Base):
    details_path: Optional[str] = None
    drivetrain: Optional[str] = None
    exterior: Optional[str] = None
    fuel_type: Optional[str] = None
    interior: Optional[str] = None
    mileage: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[str] = None
    variant: Optional[list[str]] = None
    vin: Optional[str] = None
    images: Optional[list[str]] = None
    date_listed: Optional[int] = None
    vehicle_history: Optional[str] = None
    features: Optional[Features] = None
    rating: Optional[Rating] = None
    reviews: Optional[list[CustomerReview]] = None
    price_changes: Optional[list[PriceChange]]
    average_rating: Optional[float] = None
    seller: SellerDTO


class Response(Base):
    ok: bool
    message: str


class Filter(Base):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[str] = None
    max_amount: Optional[str] = None
    sort: Optional[list] = None


class PaginationRequest(Base):
    size: int
    page: int
    filter: Optional[Filter] = None


class GetCarRequest(Base):
    vin: Optional[str] = None
    id: Optional[str] = None


class GetCarResponse(Response):
    car: Optional[CarDTO] = None


class ListCarsResponse(Response):
    total: int
    count: int
    cars: list[CarDTO] = None
