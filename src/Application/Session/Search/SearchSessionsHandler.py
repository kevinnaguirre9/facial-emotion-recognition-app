from collections.abc import Callable

from src.Application.Session.Search.SearchSessionsQuery import SearchSessionsQuery
from src.Application.Session.SessionResponse import SessionResponse
from src.Application.Session.SessionsResponse import SessionsResponse
from src.Domain.Common.Contracts.QueryHandler import QueryHandler
from src.Domain.Session.Contracts.SessionRepository import SessionRepository
from src.Domain.Session.Session import Session


class SearchSessionsHandler(QueryHandler):

    def __init__(self, repository: SessionRepository):
        self.__repository = repository

    def handle(self, query: SearchSessionsQuery) -> SessionsResponse:
        sessions = self.__repository.search(
            query.filters(),
            query.per_page(),
            query.page()
        )

        return SessionsResponse(
            list(map(self.to_response(), sessions))
        )

    @classmethod
    def to_response(cls) -> Callable[[Session], SessionResponse]:
        return lambda session_entity: SessionResponse(
            session_entity.session_id().value(),
            session_entity.class_id().value(),
            session_entity.start_date().isoformat(),
            session_entity.end_date().isoformat(),
        )