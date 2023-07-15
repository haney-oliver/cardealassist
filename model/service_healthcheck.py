from pydantic import BaseModel


class HealthcheckResponse(BaseModel):
    ok: bool
    message: str
