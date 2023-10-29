import requests
from util.logging_utils import logger
from model.cars import ListCarsRequest, ListCarsResponse
from sqlalchemy import select
from db.model import Car

async def list_cars(req: ListCarsRequest, session):
    logger.info("Fetching cars...")
    statement = select(Car).offset(req.page * req.size).limit(req.size)
    cars_query_result=session.scalars(statement)
    cars = [car.as_dto() for car in cars_query_result]
    return cars
    
