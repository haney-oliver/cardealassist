import requests
from util.logging_utils import logger
from model.cars import ListCarsRequest, ListCarsResponse, CarDTO
from sqlalchemy import select


async def list_cars(req: ListCarsRequest, collection):
    logger.info("Fetching cars...") 
    cars = collection.find()
    cars = [CarDTO(**car) for car in cars_query_result]
    return cars
    
