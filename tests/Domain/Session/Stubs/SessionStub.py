from datetime import datetime

from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Domain.Session.Session import Session
from src.Domain.Session.ValueObjects.SessionId import SessionId


class SessionStub:

    def __init__(
            self,
            session_id: SessionId|None = None,
            class_id: ClassId|None = None,
            created_at: datetime|None = None,
            started_at: datetime|None = None,
            ended_at: datetime|None = None,
    ):
        self.__session_id = session_id
        self.__class_id = class_id
        self.__created_at = created_at
        self.__started_at = started_at
        self.__ended_at = ended_at

    def get(self):
        return Session(
            self.__session_id or SessionId(),
            self.__class_id or ClassId(),
            self.__created_at or datetime.now(),
            self.__started_at or None,
            self.__ended_at or None,
        )