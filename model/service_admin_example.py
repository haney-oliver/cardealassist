from model.base import Base


class AdminRequest(Base):
    flag: bool


class AdminResponse(Base):
    message: str
