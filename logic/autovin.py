from pymongo.collection import Collection
from pymongo.results import InsertOneResult
from logic.helper.carapi import CarAPI
from model.vin import VinInfo
import util.config as cfg
from util.logging_utils import logger


client: CarAPI = CarAPI(
    api_token=cfg.CAR_API_TOKEN, api_secret=cfg.CAR_API_SECRET
)


def autovin(vin: str) -> VinInfo:
    return client.fetch_vin_info(vin)


def saveVinData(collection: Collection, vin_data: VinInfo, vin: str) -> None:
    result: InsertOneResult = collection.insert_one(document=vin_data.model_dump())
    if result.inserted_id:
        pass
    else:
        logger.error(f"Failed to write {vin}")

def checkIfExists(collection: Collection, vin: str) -> VinInfo | None:
    result = collection.find_one({"vin": vin})
    if result:
        return VinInfo(**result)


