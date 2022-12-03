from unittest import TestCase

from src.Domain.Class.Class import Class
from src.Domain.Class.Entities.Schedule import Schedule
from src.Domain.Class.Exceptions.DuplicatedDailySchedule import DuplicatedDailySchedule
from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Domain.Class.ValueObjects.DailySchedule import DailySchedule
from src.Domain.Class.ValueObjects.Weekday import Weekday
from datetime import time


class ClassEntityTest(TestCase):

    def test_should_create_entity_without_duplicate_daily_schedule(self):

        with self.assertRaises(DuplicatedDailySchedule):
            Class.create(
                ClassId(),
                'Test subject',
                'Test degree',
                'Test section',
                'Test academic period',
                Schedule(
                    [
                        DailySchedule(Weekday.MONDAY,  time(8, 0), time(10, 0)),
                        DailySchedule(Weekday.WEDNESDAY, time(8, 0), time(10, 0)),
                        DailySchedule(Weekday.MONDAY, time(8, 0), time(10, 0)),
                    ]
                )
            )