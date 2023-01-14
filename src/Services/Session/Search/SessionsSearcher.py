from collections.abc import Callable

from src.Domain.Class.Contracts.ClassRepository import ClassRepository
from src.Services.Class.Find.ClassFinder import ClassFinder
from src.Services.Class.Find.FindClassQuery import FindClassQuery
from src.Services.Session.Search.SearchSessionsQuery import SearchSessionsQuery
from src.Services.Session.SessionResponse import SessionResponse
from src.Services.Session.SessionsResponse import SessionsResponse
from src.Domain.Session.Contracts.SessionRepository import SessionRepository
from src.Domain.Session.Session import Session


class SessionsSearcher:

    def __init__(
            self,
            session_repository: SessionRepository,
            class_repository: ClassRepository,
    ):
        self.__session_repository = session_repository
        self.__class_finder = ClassFinder(class_repository)


    def handle(self, query: SearchSessionsQuery) -> SessionsResponse:

        sessions = self.__session_repository.search(
            query.filters(),
            query.per_page(),
            query.page()
        )

        return SessionsResponse(
            list(map(self.to_response, sessions))
        )


    def to_response(self, session_entity: Session) -> SessionResponse:

        class_entity = self.__class_finder.handle(
            FindClassQuery(session_entity.class_id().value())
        )

        return SessionResponse(
            session_entity.session_id().value(),
            class_entity.subject(),
            class_entity.degree(),
            session_entity.start_date().strftime('%Y-%m-%d %H:%M:%S'),
            session_entity.end_date().strftime('%Y-%m-%d %H:%M:%S') if session_entity.end_date() else None,
        )