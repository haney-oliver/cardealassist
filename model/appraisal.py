from typing import Optional

from model.base import Base


class AppraisalRequest(Base):
    year: int
    make: str
    model: str
    mileage: int
    zip_code: int


class AppraisalResponse(Base):
    value_range: Optional[str] = None
    valid: bool
