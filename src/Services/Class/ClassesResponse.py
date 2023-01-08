from src.Services.Class.ClassResponse import ClassResponse


class ClassesResponse:

    def __init__(self, classes: list[ClassResponse] = None):
        self.__classes = classes

    def classes(self) -> list[ClassResponse]:
        return self.__classes