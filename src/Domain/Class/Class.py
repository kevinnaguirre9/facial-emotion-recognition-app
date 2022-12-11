from datetime import datetime

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
            schedule: Schedule,
            created_at: datetime,
    ):
        super().__init__(class_id)
        self.__class_id = class_id
        self.__subject = subject
        self.__degree = degree
        self.__section = section
        self.__academic_period = academic_period
        self.__schedule = schedule
        self.__created_at = created_at


    @staticmethod
    def create(
            class_id: ClassId,
            subject: str,
            degree: str,
            section: str,
            academic_period: str,
            schedule: Schedule
    ):
        return Class(class_id, subject, degree, section, academic_period, schedule, datetime.now())

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

    def created_at(self) -> datetime:
        return self.__created_at

    def to_primitives(self) -> dict:
        return {
            'class_id': self.class_id().value(),
            'subject': self.subject(),
            'degree': self.degree(),
            'section': self.section(),
            'academic_period': self.academic_period(),
            'schedule': self.schedule().to_primitives(),
            'created_at': self.created_at().isoformat(),
        }

    @classmethod
    def from_primitives(cls, class_data: dict) -> 'Class':
        return cls(
            ClassId(class_data['class_id']),
            class_data['subject'],
            class_data['degree'],
            class_data['section'],
            class_data['academic_period'],
            Schedule.from_primitives(class_data['schedule']),
            datetime.fromisoformat(class_data['created_at'])
        )