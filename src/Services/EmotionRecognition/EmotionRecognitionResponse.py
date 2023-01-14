
class EmotionRecognitionResponse:

    def __init__(
            self,
            emotion_recognition_id: str,
            session_id: str,
            angry: int,
            disgusted: int,
            fearful: int,
            happy: int,
            neutral: int,
            sad: int,
            surprised: int,
            recorded_at: str,
    ):
        self.__emotion_recognition_id = emotion_recognition_id
        self.__session_id = session_id
        self.__angry = angry
        self.__disgusted = disgusted
        self.__fearful = fearful
        self.__happy = happy
        self.__neutral = neutral
        self.__sad = sad
        self.__surprised = surprised
        self.__recorded_at = recorded_at


    def emotion_recognition_id(self) -> str:
        return self.__emotion_recognition_id


    def session_id(self) -> str:
        return self.__session_id


    def angry(self) -> int:
        return self.__angry


    def disgusted(self) -> int:
        return self.__disgusted


    def fearful(self) -> int:
        return self.__fearful


    def happy(self) -> int:
        return self.__happy


    def neutral(self) -> int:
        return self.__neutral


    def sad(self) -> int:
        return self.__sad


    def surprised(self) -> int:
        return self.__surprised


    def recorded_at(self) -> str:
        return self.__recorded_at
