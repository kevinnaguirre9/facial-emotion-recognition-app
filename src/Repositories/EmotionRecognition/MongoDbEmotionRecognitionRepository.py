from collections.abc import Callable

from src.Domain.EmotionRecognition.Contracts.EmotionRecognitionRepository import EmotionRecognitionRepository
from src.Domain.EmotionRecognition.EmotionRecognition import EmotionRecognition
from src.Domain.EmotionRecognition.ValueObjects.EmotionRecognitionId import EmotionRecognitionId
from src.Repositories.Common.MongoDBClient import MongoDBClient


class MongoDbEmotionRecognitionRepository(EmotionRecognitionRepository):

    COLLECTION_NAME = 'emotion_recognitions'

    def __init__(self, mongo_client: MongoDBClient):
        self.__mongo_client = mongo_client.get_db_connection()


    def save(self, emotion_recognition_entity: EmotionRecognition):
        self.__mongo_client[self.COLLECTION_NAME] \
            .update_one(
            {'emotion_recognition_id': emotion_recognition_entity.emotion_recognition_id().value()},
            {'$set': emotion_recognition_entity.to_primitives()},
            upsert=True
        )


    def find(self, emotion_recognition_id: EmotionRecognitionId) -> EmotionRecognition | None:
        emotion_recognition_entity = self.__mongo_client[self.COLLECTION_NAME] \
            .find_one({'emotion_recognition_id': emotion_recognition_id.value()})

        if emotion_recognition_entity is None:
            return None

        return self.__to_entity()(dict(emotion_recognition_entity))


    def search(self, criteria: dict, limit: int|None, page: int|None) -> list[EmotionRecognition]|None:
        emotion_recognitions = self.__mongo_client[self.COLLECTION_NAME] \
            .find(criteria) \

        if limit is not None and page is not None:
            emotion_recognitions\
                .skip((page - 1) * limit) \
                .limit(limit)

        return list(map(self.__to_entity(), emotion_recognitions))


    def delete(self, emotion_recognition_entity: EmotionRecognition) -> None:
        self.__mongo_client[self.COLLECTION_NAME] \
            .delete_one({'emotion_recognition_id': emotion_recognition_entity.emotion_recognition_id().value()})


    @classmethod
    def __to_entity(cls) -> Callable[[dict], EmotionRecognition]:
        return lambda emotion_recognition_data: EmotionRecognition.from_primitives(emotion_recognition_data)