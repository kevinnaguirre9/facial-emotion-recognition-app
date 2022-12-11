from enum import Enum


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @staticmethod
    def from_name(weekday_name: str) -> 'Weekday':
        return Weekday[weekday_name.upper()]

    @staticmethod
    def from_value(weekday_value: int) -> 'Weekday':
        return Weekday(weekday_value)

