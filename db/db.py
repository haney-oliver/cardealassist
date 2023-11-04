from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from util.config import settings
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

print(f"\nSettings:\n{settings.__dict__}\n\n")
DATABASE_URL = f"mongodb+srv://{settings.databaseUser}:{settings.databasePassword}@{settings.databaseHost}"


class DatabaseClient:
    def __init__(self):
        self.mongodb_client = MongoClient(DATABASE_URL)

    def fetch_database(self, db_name: str) -> Database:
        return self.mongodb_client[db_name]

    def fetch_collection(self, db: Database, collection_name: str) -> Collection:
        return db[collection_name]
