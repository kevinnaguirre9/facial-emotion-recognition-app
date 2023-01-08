
class CrateClassCommand:

    def __init__(
            self,
            subject: str,
            degree: str,
            section: str,
            academic_period: str,
            weekly_schedule: list,
    ):
        self.__subject = subject
        self.__degree = degree
        self.__section = section
        self.__academic_period = academic_period
        self.__weekly_schedule = weekly_schedule


    def subject(self) -> str:
        return self.__subject

    def degree(self) -> str:
        return self.__degree

    def section(self) -> str:
        return self.__section

    def academic_period(self) -> str:
        return self.__academic_period

    def weekly_schedule(self) -> list:
        return self.__weekly_schedule