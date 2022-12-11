from collections.abc import Callable

from src.Domain.Class.Class import Class
from src.Domain.Class.Contracts.ClassRepository import ClassRepository
from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Infrastructure.Common.MongoDBClient import MongoDBClient


class MongoDbClassRepository(ClassRepository):

    COLLECTION_NAME = 'classes'

    def __init__(self, mongo_client: MongoDBClient):
        self.__mongo_client = mongo_client.get_connection()


    def save(self, class_entity: Class):
        self.__mongo_client[self.COLLECTION_NAME]\
            .update_one(
                {'class_id': class_entity.class_id().value()},
                {'$set': class_entity.to_primitives()},
                upsert=True
            )


    def find(self, class_id: ClassId) -> Class | None:
        class_entity = self.__mongo_client[self.COLLECTION_NAME]\
            .find_one({'class_id': class_id.value()})

        if class_entity is None:
            return None

        return self.to_entity()(dict(class_entity))


    def search(self, criteria: dict, limit: int, page: int) -> list[Class]|None:
        classes = self.__mongo_client[self.COLLECTION_NAME]\
            .find(criteria)\
            .sort('created_at', -1)\
            .skip((page - 1) * limit)\
            .limit(limit)

        return list(map(self.to_entity(), classes))


    def delete(self, class_entity: Class) -> None:
        self.__mongo_client[self.COLLECTION_NAME]\
            .delete_one({'class_id': class_entity.class_id().value()})

    @classmethod
    def to_entity(cls) -> Callable[[dict], Class]:
        return lambda class_data: Class.from_primitives(class_data)