from unittest import TestCase

from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Infrastructure.Class.Repositories.MongoDbClassRepository import MongoDbClassRepository
from src.Infrastructure.Common.MongoDBClient import MongoDBClient
from tests.Domain.Class.Stubs.ClassStub import ClassStub


class MongoDbClassRepositoryTest(TestCase):

    def setUp(self) -> None:
        self.__mongo_client = MongoDBClient()
        self.__class_repository = MongoDbClassRepository(self.__mongo_client)
        self.__collection_name = self.__class_repository.COLLECTION_NAME

    def test_should_save_class(self):
        class_entity = ClassStub().get()

        self.__class_repository.save(class_entity)


    def test_should_find_class(self):
        class_entity = ClassStub().get()

        self.__class_repository.save(class_entity)

        class_found = self.__class_repository.find(class_entity.class_id())

        self.assertEqual(class_found, class_entity)


    def test_should_return_none_when_class_not_found(self):
        class_found = self.__class_repository.find(ClassId())

        self.assertIsNone(class_found)


    def test_should_search_classes(self):
        class_entity = ClassStub(
            academic_period='2021-2022'
        ).get()

        self.__class_repository.save(class_entity)

        # todo: test with more filters
        classes_found = self.__class_repository.search({
            'academic_period': '2021-2022'
        }, limit=10, page=1)

        self.assertTrue(len(classes_found) > 0)


    def test_should_delete_class(self):
        class_entity = ClassStub().get()

        self.__class_repository.save(class_entity)

        self.__class_repository.delete(class_entity)

        class_found = self.__class_repository.find(class_entity.class_id())

        self.assertIsNone(class_found)


    def tearDown(self) -> None:
        self.__mongo_client.get_connection()[self.__collection_name].delete_many({})
        self.__mongo_client.close_connection()



