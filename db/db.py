from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from util.config import settings
from pymongo import MongoClient

print(f"\nSettings:\n{settings.__dict__}\n\n")
DATABASE_URL = f"mongodb+srv://{settings.databaseUser}:{settings.databasePassword}@{settings.databaseHost}/{settings.databaseName}"



class MongoDatabaseClient:
    def __init__(self):
        self.mongodb_client = MongoClient(DATABASE_URL)

    def fetch_collection(self, collection_name):
        return self.mongodb_client[collection_name]

    

