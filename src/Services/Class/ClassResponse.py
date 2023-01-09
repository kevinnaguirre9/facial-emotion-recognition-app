
class ClassResponse:

    def __init__(
            self,
            class_id: str,
            subject: str,
            degree: str,
            section: str,
            academic_period: str,
    ):
        self.__class_id = class_id
        self.__subject = subject
        self.__degree = degree
        self.__section = section
        self.__academic_period = academic_period

    def class_id(self) -> str:
        return self.__class_id

    def subject(self) -> str:
        return self.__subject

    def degree(self) -> str:
        return self.__degree

    def section(self) -> str:
        return self.__section

    def academic_period(self) -> str:
        return self.__academic_period