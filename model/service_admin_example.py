from pydantic import BaseModel


class AdminRequest(BaseModel):
    flag: bool


class AdminResponse(BaseModel):
    message: str
