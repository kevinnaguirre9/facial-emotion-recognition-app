from datetime import time
from src.Domain.Class.ValueObjects.Weekday import Weekday


class DailySchedule:
    def __init__(self, day: Weekday, start_time: time, end_time: time):
        self.__day = day
        self.__start_time = start_time
        self.__end_time = end_time

    def day(self) -> Weekday:
        return self.__day

    def start_time(self) -> time:
        return self.__start_time

    def end_time(self) -> time:
        return self.__end_time

    def __eq__(self, other: 'DailySchedule') -> bool:
        return self.__day == other.__day

    def to_primitives(self) -> dict:
        return {
            'day': self.__day.value,
            'start_time': self.__start_time.strftime('%H:%M'),
            'end_time': self.__end_time.strftime('%H:%M')
        }