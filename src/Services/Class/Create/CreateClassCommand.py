
class CreateClassCommand:

    def __init__(
            self,
            subject: str,
            degree: str,
            section: str,
            academic_period: str,
    ):
        self.__subject = subject
        self.__degree = degree
        self.__section = section
        self.__academic_period = academic_period


    def subject(self) -> str:
        return self.__subject

    def degree(self) -> str:
        return self.__degree

    def section(self) -> str:
        return self.__section

    def academic_period(self) -> str:
        return self.__academic_period