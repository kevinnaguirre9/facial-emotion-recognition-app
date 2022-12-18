from collections.abc import Callable

from src.Domain.Session.Contracts.SessionRepository import SessionRepository
from src.Domain.Session.Session import Session
from src.Domain.Session.ValueObjects.SessionId import SessionId
from src.Infrastructure.Common.MongoDBClient import MongoDBClient


class MongoDbSessionRepository(SessionRepository):

    COLLECTION_NAME = 'sessions'

    def __init__(self, mongo_client: MongoDBClient):
        self.__mongo_client = mongo_client.get_connection()


    def save(self, session_entity: Session):
        self.__mongo_client[self.COLLECTION_NAME] \
            .update_one(
            {'session_id': session_entity.session_id().value()},
            {'$set': session_entity.to_primitives()},
            upsert=True
        )


    def find(self, session_id: SessionId) -> Session | None:
        session_entity = self.__mongo_client[self.COLLECTION_NAME] \
            .find_one({'session_id': session_id.value()})

        if session_entity is None:
            return None

        return self.__to_entity()(dict(session_entity))


    def search(self, criteria: dict, limit: int, page: int) -> list[Session] | None:
        sessions = self.__mongo_client[self.COLLECTION_NAME] \
            .find(criteria) \
            .sort('created_at', -1) \
            .skip((page - 1) * limit) \
            .limit(limit)

        return list(map(self.__to_entity(), sessions))


    def delete(self, session_entity: Session) -> None:
        self.__mongo_client[self.COLLECTION_NAME] \
            .delete_one({'session_id': session_entity.session_id().value()})


    @classmethod
    def __to_entity(cls) -> Callable[[dict], Session]:
        return lambda session_data: Session.from_primitives(session_data)