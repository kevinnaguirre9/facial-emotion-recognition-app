from datetime import time
import random

from src.Domain.Class.ValueObjects.DailySchedule import DailySchedule
from src.Domain.Class.ValueObjects.Weekday import Weekday


class DailyScheduleStub:

    def __init__(self, day: Weekday|None = None, start_time: time|None = None, end_time: time|None = None):
        self.__day = day
        self.__start_time = start_time
        self.__end_time = end_time


    def get(self) -> DailySchedule:

        return DailySchedule(
            self.__day or Weekday(random.choice([e.value for e in Weekday])),
            self.__start_time or time(8, 0),
            self.__end_time or time(10, 0)
        )