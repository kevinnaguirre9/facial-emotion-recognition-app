from src.Application.Session.Create.CreateSessionCommand import CreateSessionCommand
from src.Domain.Class.Class import Class
from src.Domain.Class.Contracts.ClassRepository import ClassRepository
from src.Domain.Class.Exceptions.ClassNotFound import ClassNotFound
from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Domain.Common.Contracts.CommandHandler import CommandHandler
from src.Domain.Session.Contracts.SessionRepository import SessionRepository
from src.Domain.Session.Session import Session
from src.Domain.Session.ValueObjects.SessionId import SessionId


class CreateSessionHandler(CommandHandler):

    def __init__(
            self,
            session_repository: SessionRepository,
            class_repository: ClassRepository,
    ):
        self.__session_repository = session_repository
        self.__class_repository = class_repository


    def handle(self, command: CreateSessionCommand):

        class_entity = self.__class_repository.find(
            ClassId(command.class_id())
        )

        self.__ensure_class_exists(class_entity)

        session = Session.create(
            SessionId(),
            class_entity.class_id(),
        )

        self.__session_repository.save(session)

        return session


    @classmethod
    def __ensure_class_exists(cls, class_entity: Class|None):
        if class_entity is None:
            raise ClassNotFound()
