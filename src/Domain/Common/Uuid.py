import uuid


class Uuid:
    def __init__(self, value: str = None):
        if value is None:
            value = self.generate()
        self.__value = value

    @staticmethod
    def generate() -> str:
        return str(uuid.uuid4())

    def value(self) -> str:
        return self.__value

    def __str__(self) -> str:
        return self.value()

    def __eq__(self, other: 'Uuid') -> bool:
        return self.value() == other.value()

