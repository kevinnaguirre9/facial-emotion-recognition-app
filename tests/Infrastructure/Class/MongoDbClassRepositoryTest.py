from unittest import TestCase

from src.Infrastructure.Class.Repositories.MongoDbClassRepository import MongoDbClassRepository
from src.Infrastructure.Common.MongoDBClient import MongoDBClient
from tests.Domain.Class.Stubs.ClassStub import ClassStub


class MongoDbClassRepositoryTest(TestCase):

    def setUp(self) -> None:
        self.__mongo_client = MongoDBClient()
        self.__class_repository = MongoDbClassRepository(self.__mongo_client)
        self.__collection_name = self.__class_repository.COLLECTION_NAME

    def test_should_save_class_happy_path(self):
        class_entity = ClassStub().get()

        self.__class_repository.save(class_entity)

    def tearDown(self) -> None:
        self.__mongo_client.get_connection()[self.__collection_name].delete_many({})
        self.__mongo_client.close_connection()



