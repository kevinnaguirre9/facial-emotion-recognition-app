import json
from unittest import TestCase

from src.Domain.Class.Exceptions.DuplicatedDailySchedule import DuplicatedDailySchedule
from src.Domain.Class.ValueObjects.Weekday import Weekday
from tests.Domain.Class.Stubs.ClassStub import ClassStub
from tests.Domain.Class.Stubs.DailyScheduleStub import DailyScheduleStub
from tests.Domain.Class.Stubs.ScheduleStub import ScheduleStub


class ClassEntityTest(TestCase):

    def test_should_throw_exception_when_creating_class_with_duplicate_daily_schedules(self):

        with self.assertRaises(DuplicatedDailySchedule):
            ClassStub(
                schedule=ScheduleStub([
                        DailyScheduleStub(day = Weekday.WEDNESDAY).get(),
                        DailyScheduleStub(day = Weekday.WEDNESDAY).get(),
                    ]).get()
            ).get()