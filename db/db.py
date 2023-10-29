from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from util.config import settings

print(f"\nSettings:\n{settings.__dict__}\n\n")
DATABASE_URL = f"mysql+pymysql://{settings.databaseUser}:{settings.databasePassword}@{settings.databaseHost}:3307/{settings.databaseName}"


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, echo=False)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self, base):
        base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

    def get_engine(self):
        return self.engine
