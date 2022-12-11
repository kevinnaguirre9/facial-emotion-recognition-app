from pymongo import MongoClient
from pymongo.database import Database

import config.database as db_config

class MongoDBClient:

    def __init__(self):
        self.__client = MongoClient(db_config.MONGO_DB_URI)

    def get_connection(self) -> Database:
        return self.__client[db_config.MONGO_DB_NAME]

    def close_connection(self):
        self.__client.close()

