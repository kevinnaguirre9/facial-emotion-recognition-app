from dependency_injector import containers, providers
from pymongo import MongoClient
import logging.config

import config.database as db_config
from src.Repositories.Class.MongoDbClassRepository import MongoDbClassRepository
from src.Repositories.Common.MongoDBClient import MongoDBClient
from src.Repositories.EmotionRecognition.MongoDbEmotionRecognitionRepository import MongoDbEmotionRecognitionRepository
from src.Repositories.Session.MongoDbSessionRepository import MongoDbSessionRepository


class ServiceContainer(containers.DeclarativeContainer):

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    pymongo_mongo_client = providers.Singleton(
        MongoClient,
        host = db_config.MONGO_DB_URI,
    )

    mongo_db_repository_client = providers.Factory(
        MongoDBClient,
        mongo_client = pymongo_mongo_client,
        database_name = db_config.MONGO_DB_NAME
    )

    emotion_recognition_repository = providers.Factory(
        MongoDbEmotionRecognitionRepository,
        mongo_client = mongo_db_repository_client
    )

    class_repository = providers.Factory(
        MongoDbClassRepository,
        mongo_client = mongo_db_repository_client
    )

    session_repository = providers.Factory(
        MongoDbSessionRepository,
        mongo_client = mongo_db_repository_client
    )

    # emotion_recognizer_register = providers.Factory(
    #     EmotionRecognitionRegister,
    #     emotion_recognition_repository = mongo_db_emotion_recognition_repository
    # )


