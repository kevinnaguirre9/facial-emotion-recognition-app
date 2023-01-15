
class SessionResponse:

    def __init__(
            self,
            session_id: str,
            class_subject: str,
            class_degree: str,
            started_at: str,
            ended_at: str|None = None,
    ):
        self.__session_id = session_id
        self.__class_subject = class_subject
        self.__class_degree = class_degree
        self.__started_at = started_at
        self.__ended_at = ended_at

    def session_id(self) -> str:
        return self.__session_id

    def class_subject(self) -> str:
        return self.__class_subject

    def class_degree(self) -> str:
        return self.__class_degree

    def started_at(self) -> str:
        return self.__started_at

    def ended_at(self) -> str|None:
        return self.__ended_at