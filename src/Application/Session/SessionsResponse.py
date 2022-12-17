from src.Application.Session.SessionResponse import SessionResponse


class SessionsResponse:

    def __init__(self, sessions: list[SessionResponse]):
        self.__sessions = sessions

    def sessions(self) -> list[SessionResponse]:
        return self.__sessions