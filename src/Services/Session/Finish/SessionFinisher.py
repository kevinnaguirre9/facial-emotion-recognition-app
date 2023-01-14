from src.Domain.Session.Contracts.SessionRepository import SessionRepository
from src.Domain.Session.ValueObjects.SessionId import SessionId
from src.Services.Session.Finish.FinishSessionCommand import FinishSessionCommand


class SessionFinisher:

    def __init__(self, session_repository: SessionRepository):
        self.session_repository = session_repository

    def handle(self, command: FinishSessionCommand):
        session = self.session_repository.find(SessionId(command.session_id()))

        session.end()

        self.session_repository.save(session)