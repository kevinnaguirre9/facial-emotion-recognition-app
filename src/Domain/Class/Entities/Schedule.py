from src.Domain.Class.Exceptions.DuplicatedDailySchedule import DuplicatedDailySchedule
from src.Domain.Class.ValueObjects.DailySchedule import DailySchedule


class Schedule:
    def __init__(self, weekly_schedule: list[DailySchedule]):
        self.__validate_weekly_schedule(weekly_schedule)
        self.__weekly_schedule = weekly_schedule

    @staticmethod
    def __validate_weekly_schedule(weekly_schedule: list[DailySchedule]):
        schedule_days = []

        for daily_schedule in weekly_schedule:
            if daily_schedule in schedule_days:
                raise DuplicatedDailySchedule(daily_schedule.day())

            schedule_days.append(daily_schedule)

        schedule_days.clear()