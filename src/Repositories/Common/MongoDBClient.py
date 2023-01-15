from pymongo import MongoClient
from pymongo.database import Database

import config.database as db_config

class MongoDBClient:

    def __init__(self, mongo_client: MongoClient, database_name: str):
        self.__db_connection = mongo_client[database_name]

    def get_db_connection(self) -> Database:
        return self.__db_connection

