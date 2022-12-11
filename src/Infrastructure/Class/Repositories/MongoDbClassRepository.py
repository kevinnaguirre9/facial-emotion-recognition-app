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
        pass

    def search(self, criteria: list) -> list[Class]:
        pass

    def delete(self, class_entity: Class) -> None:
        pass