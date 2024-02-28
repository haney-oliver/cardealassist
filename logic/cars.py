import requests
from util.logging_utils import logger
from model.cars import (
    PaginationRequest,
    ListCarsResponse,
    CarDTO,
    GetCarRequest,
    GetCarResponse,
)


async def list_cars(req: PaginationRequest, collection) -> ListCarsResponse:
    limit = req.size
    page = req.page
    if req.filter:
        query = {}
        if req.filter.make:
            query["make"] = req.filter.make
        if req.filter.model:
            query["model"] = req.filter.model
        if req.filter.max_amount:
            query["price"] = {"$lt": req.filter.max_amount}
        if req.filter.year:
            query["year"] = req.filter.year
        sort = req.filter.sort if req.filter.sort else None
    else:
        query = {}
        sort = None
    total = collection.count_documents(query)
    if sort:
        cars = (
            collection.find(filter=query, skip=page * limit)
            .limit(limit)
            .sort([sort])
        )
    else:
        cars = collection.find(filter=query, skip=page * limit).limit(limit)
    cars = list(cars)
    cars = [CarDTO(**car) for car in cars]
    for car in cars:
        rating_sum: int = 0
        if len(car.reviews) > 0:
            for review in car.reviews:
                rating_sum += review.rating
            car.average_rating = rating_sum / len(car.reviews)
    return ListCarsResponse(
        cars=cars,
        total=total,
        count=len(cars),
        ok=True,
        message="Successfully fetched cars.",
    )


async def get_car(req: GetCarRequest, collection) -> GetCarResponse:
    car = None
    if req.id:
        car = collection.find_one({"_id": req.id})
    elif req.vin:
        car = collection.find_one({"vin": req.vin})

    if car:
        return GetCarResponse(
            car=CarDTO(**car), ok=True, message="Successfully fetched car."
        )
    else:
        search_term = f"VIN: {req.vin}" if req.vin else f"ID: {req.id}"
        return GetCarResponse(
            ok=True, message=f"Could not find any cars with {search_term}"
        )
