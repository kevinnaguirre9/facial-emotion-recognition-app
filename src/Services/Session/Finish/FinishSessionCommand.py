
class FinishSessionCommand:

    def __init__(self, session_id: str):
        self.__session_id = session_id

    def session_id(self) -> str:
        return self.__session_id