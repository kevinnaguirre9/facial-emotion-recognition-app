from src.Domain.Session.Contracts.SessionRepository import SessionRepository
from src.Domain.Session.ValueObjects.SessionId import SessionId
from src.Services.Session.Finish.FinishSessionCommand import FinishSessionCommand


class SessionFinisher:
    def __init__(self, session_repository: SessionRepository, session_id: str):
        self.__session_repository = session_repository
        self.__session_id = session_id

    def handle(self):
        session = self.__session_repository.find(SessionId(self.__session_id))

        print('------------------ handle')

        session.end()

        print(session.to_primitives())

        self.__session_repository.save(session)