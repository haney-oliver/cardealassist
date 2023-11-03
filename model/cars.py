from pydantic import BaseModel
from dataclasses import dataclass

class ListCarsRequest(BaseModel):
    page: int
    size: int


class ListCarsResponse(BaseModel):
    ok: bool
    message: str
    cars: list[str]

@dataclass
class CarDTO(BaseModel):
    id: str
    details_path: str = None
    drivetrain: str = None
    exterior: str = None
    fuel_type: str = None
    interior: str = None
    mileage: str = None
    price: str = None
    source: str = None
    title: str = None
    vin: str = None
    seller_id: str = None
