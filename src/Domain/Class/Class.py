from src.Domain.Common.BaseEntity import BaseEntity
from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Domain.Class.Entities.Schedule import Schedule


class Class(BaseEntity):
    def __init__(
            self,
            class_id: ClassId,
            subject: str,
            degree: str,
            section: str,
            academic_period: str,
            schedule: Schedule
    ):
        super().__init__(class_id)
        self.__class_id = class_id
        self.__subject = subject
        self.__degree = degree
        self.__section = section
        self.__academic_period = academic_period
        self.__schedule = schedule


    @staticmethod
    def create(
            class_id: ClassId,
            subject: str,
            degree: str,
            section: str,
            academic_period: str,
            schedule: Schedule
    ):
        return Class(class_id, subject, degree, section, academic_period, schedule)

    def class_id(self) -> ClassId:
        return self.__class_id

    def subject(self) -> str:
        return self.__subject

    def degree(self) -> str:
        return self.__degree

    def section(self) -> str:
        return self.__section

    def academic_period(self) -> str:
        return self.__academic_period

    def schedule(self) -> Schedule:
        return self.__schedule