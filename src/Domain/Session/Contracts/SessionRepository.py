from abc import ABC, abstractmethod

from src.Domain.Session.Session import Session
from src.Domain.Session.ValueObjects.SessionId import SessionId


class SessionRepository(ABC):
    @abstractmethod
    def save(self, session_entity: Session):
        pass

    @abstractmethod
    def find(self, session_id: SessionId) -> Session|None:
        pass

    @abstractmethod
    def search(self, criteria: dict, limit: int, page: int) -> list[Session]|None:
        pass

    @abstractmethod
    def delete(self, session_entity: Session) -> None:
        pass