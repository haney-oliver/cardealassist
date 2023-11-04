import requests
from util.logging_utils import logger
from model.cars import (
    ListCarsRequest,
    ListCarsResponse,
    CarDTO,
    GetCarRequest,
    GetCarResponse,
)
from sqlalchemy import select


async def list_cars(req: ListCarsRequest, collection) -> ListCarsResponse:
    cars = collection.find(req.filter)
    return ListCarsResponse(cars=[CarDTO(**car) for car in cars], ok=True, message="Successfully fetched cars.")


async def get_car(req: GetCarRequest, collection) -> GetCarResponse:
    car = None
    if req.id:
        car = collection.find_one({"_id": req.id})
    elif req.vin:
        car = collection.find_one({"vin": req.vin})

    if car:
        return GetCarResponse(car=CarDTO(**car), ok=True, message="Successfully fetched car.")
    else:
        search_term = f"VIN: {req.vin}" if req.vin else f"ID: {req.id}"
        return GetCarResponse(ok=True, message=f"Could not find any cars with {search_term}")
