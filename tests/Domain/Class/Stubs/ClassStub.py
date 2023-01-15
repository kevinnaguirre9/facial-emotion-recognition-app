import random
from datetime import datetime

from faker import Faker

from src.Domain.Class.Class import Class
from src.Domain.Class.Entities.Schedule import Schedule
from src.Domain.Class.ValueObjects.ClassId import ClassId
from tests.Domain.Class.Stubs.ScheduleStub import ScheduleStub


class ClassStub:

    def __init__(
            self,
            class_id: ClassId|None = None,
            subject: str|None = None,
            degree: str|None = None,
            section: str|None = None,
            academic_period: str|None = None,
            schedule: Schedule|None = None,
            create_at: datetime|None = None,
    ):
        self.__class_id = class_id
        self.__subject = subject
        self.__degree = degree
        self.__section = section
        self.__academic_period = academic_period
        self.__schedule = schedule
        self.__create_at = create_at


    def get(self) -> Class:

        faker = Faker()

        return Class(
            self.__class_id or ClassId(),
            self.__subject or faker.word(),
            self.__degree or faker.word(),
            self.__section or faker.word(),
            self.__academic_period or random.choice(['2021-2022', '2022-2023']),
            self.__schedule or ScheduleStub().get(),
            self.__create_at or datetime.now()
        )