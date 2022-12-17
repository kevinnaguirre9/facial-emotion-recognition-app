from datetime import datetime

from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Domain.Common.BaseEntity import BaseEntity
from src.Domain.Session.ValueObjects.SessionId import SessionId


class Session(BaseEntity):
    def __init__(
            self,
            session_id: SessionId,
            class_id: ClassId,
            created_at: datetime,
            started_at: datetime|None = None,
            ended_at: datetime|None = None,
    ):
        super().__init__(session_id)
        self.__session_id = session_id
        self.__class_id = class_id
        self.__created_at = created_at
        self.__started_at = started_at
        self.__ended_at = ended_at


    @staticmethod
    def create(
            session_id: SessionId,
            class_id: ClassId,
    ):
        return Session(session_id, class_id, datetime.now())

    def session_id(self) -> SessionId:
        return self.__session_id

    def class_id(self) -> ClassId:
        return self.__class_id

    def creation_date(self) -> datetime:
        return self.__created_at

    def start(self):
        self.__started_at = datetime.now()

    def end(self):
        self.__ended_at = datetime.now()

    def start_date(self) -> datetime|None:
        return self.__started_at

    def end_date(self) -> datetime|None:
        return self.__ended_at

    def to_primitive(self):
        return {
            'session_id': self.session_id().value(),
            'class_id': self.class_id().value(),
            'created_at': self.creation_date().isoformat(),
            'started_at': self.start_date().isoformat(),
            'ended_at': self.end_date().isoformat(),
        }

    @classmethod
    def from_primitive(cls, session_data: dict) -> 'Session':
        return cls(
            SessionId(session_data['session_id']),
            ClassId(session_data['class_id']),
            datetime.fromisoformat(session_data['created_at']),
            datetime.fromisoformat(session_data['started_at']) if session_data['started_at'] else None,
            datetime.fromisoformat(session_data['ended_at']) if session_data['ended_at'] else None,
        )