
class RegisterEmotionRecognitionCommand:

    def __init__(self, frame, session_id: str):
        self.__frame = frame
        self.__session_id = session_id

    def frame(self):
        return self.__frame

    def session_id(self) -> str:
        return self.__session_id
