
class SessionResponse:

    def __init__(
            self,
            session_id: str,
            class_id: str,
            started_at: str,
            ended_at: str,
    ):
        self.__session_id = session_id
        self.__class_id = class_id
        self.__started_at = started_at
        self.__ended_at = ended_at

    def session_id(self) -> str:
        return self.__session_id

    def class_id(self) -> str:
        return self.__class_id

    def started_at(self) -> str:
        return self.__started_at

    def ended_at(self) -> str:
        return self.__ended_at