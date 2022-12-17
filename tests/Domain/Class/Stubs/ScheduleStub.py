from src.Domain.Class.Entities.Schedule import Schedule
from src.Domain.Class.ValueObjects.DailySchedule import DailySchedule
from tests.Domain.Class.Stubs.DailyScheduleStub import DailyScheduleStub


class ScheduleStub:

    def __init__(
            self,
            weekly_schedule: list[DailySchedule]|None = None
    ):
        self.__weekly_schedule = weekly_schedule


    def get(self) -> Schedule:
        return Schedule(self.__weekly_schedule or [DailyScheduleStub().get()])