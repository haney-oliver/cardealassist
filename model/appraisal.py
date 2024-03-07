from typing import Optional

from model.base import Base


class AppraisalRequest(Base):
    year: str
    make: str
    model: str
    mileage: str
    zip_code: str


class AppraisalResponse(Base):
    value_range: Optional[str] = None
    valid: bool
