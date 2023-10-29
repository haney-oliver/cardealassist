from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType, database_exists, create_database
import uuid

from model.cars import CarDTO

Base = declarative_base()


def uuid_as_string():
    return str(uuid.uuid4())


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(String(36), primary_key=True, default=uuid_as_string)
    street = Column(String(250))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(10))
    name = Column(String(150), unique=True)
    website = Column(String(500), unique=True)
    raw_address = Column(String(500))

    car = relationship("Car", back_populates="seller")


class Car(Base):
    __tablename__ = "cars"

    id = Column(String(36), primary_key=True, default=uuid_as_string)
    details_path = Column(String(200))
    drivetrain = Column(String(50))
    exterior = Column(String(50))
    fuel_type = Column(String(50))
    interior = Column(String(50))
    mileage = Column(String(50))
    price = Column(String(50))
    source = Column(String(50))
    title = Column(String(150))
    vin = Column(String(50), unique=True)

    seller_id = Column(String(36), ForeignKey("sellers.id"))
    seller = relationship("Seller", back_populates="car")

    def as_dto(self):
        return CarDTO(
            id=self.id,
            street=self.details_path,
            drivetrain=self.drivetrain,
            exterior=self.exterior,
            fuel_type=self.fuel_type,
            mileage=self.mileage,
            price=self.price,
            source=self.source,
            title=self.title,
            vin=self.vin,
        )
