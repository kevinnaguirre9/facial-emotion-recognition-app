
class RegisterEmotionRecognitionCommand:

    def __init__(
            self,
            session_id: str,
            total_angry: int,
            total_disgusted: int,
            total_fearful: int,
            total_happy: int,
            total_neutral: int,
            total_sad: int,
            total_surprised: int
    ):
        self.__session_id = session_id
        self.__total_angry = total_angry
        self.__total_disgusted = total_disgusted
        self.__total_fearful = total_fearful
        self.__total_happy = total_happy
        self.__total_neutral = total_neutral
        self.__total_sad = total_sad
        self.__total_surprised = total_surprised

    def session_id(self) -> str:
        return self.__session_id

    def total_angry(self) -> int:
        return self.__total_angry

    def total_disgusted(self) -> int:
        return self.__total_disgusted

    def total_fearful(self) -> int:
        return self.__total_fearful

    def total_happy(self) -> int:
        return self.__total_happy

    def total_neutral(self) -> int:
        return self.__total_neutral

    def total_sad(self) -> int:
        return self.__total_sad

    def total_surprised(self) -> int:
        return self.__total_surprised
