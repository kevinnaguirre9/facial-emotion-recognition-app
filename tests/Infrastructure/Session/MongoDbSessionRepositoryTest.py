from unittest import TestCase

from src.Repositories.Common.MongoDBClient import MongoDBClient
from src.Repositories.Session.MongoDbSessionRepository import MongoDbSessionRepository
from tests.Domain.Session.Stubs.SessionStub import SessionStub


class MongoDbSessionRepositoryTest(TestCase):

    def setUp(self) -> None:
        self.__mongo_client = MongoDBClient()
        self.__session_repository = MongoDbSessionRepository(self.__mongo_client)
        self.__collection_name = self.__session_repository.COLLECTION_NAME


    def test_should_save_session(self):
        session_entity = SessionStub().get()

        self.__session_repository.save(session_entity)


    def test_should_find_session(self):
        session_entity = SessionStub().get()

        self.__session_repository.save(session_entity)

        session_found = self.__session_repository.\
            find(session_entity.session_id())

        self.assertEqual(session_found, session_entity)


    def test_should_delete_session(self):
        session_entity = SessionStub().get()

        self.__session_repository.save(session_entity)

        self.__session_repository.delete(session_entity)

        session_found = self.__session_repository.\
            find(session_entity.session_id())

        self.assertIsNone(session_found)
