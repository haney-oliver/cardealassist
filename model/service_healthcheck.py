from model.base import Base


class HealthcheckResponse(Base):
    ok: bool
    message: str
