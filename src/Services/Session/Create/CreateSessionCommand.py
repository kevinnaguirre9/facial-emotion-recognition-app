
class CreateSessionCommand:

    def __init__(self, class_id: str):
        self.__class_id = class_id

    def class_id(self) -> str:
        return self.__class_id