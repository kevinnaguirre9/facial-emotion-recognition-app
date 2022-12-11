from datetime import datetime

from src.Application.Class.Create import CreateClassCommand
from src.Domain.Class.Class import Class
from src.Domain.Class.Contracts.ClassRepository import ClassRepository
from src.Domain.Class.Entities.Schedule import Schedule
from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Domain.Class.ValueObjects.DailySchedule import DailySchedule
from src.Domain.Class.ValueObjects.Weekday import Weekday
from src.Domain.Common.Contracts.CommandHandler import CommandHandler


class CreateClassHandler(CommandHandler):

    def __init__(self, repository: ClassRepository):
        self.__repository = repository


    def handle(self, command: CreateClassCommand):

        weekly_schedule = [
            DailySchedule(
                Weekday[daily_schedule.get('weekday').upper()],
                datetime.strptime(daily_schedule.get('start_time'), '%H:%M').time(),
                datetime.strptime(daily_schedule.get('end_time'), '%H:%M').time()
            )
            for daily_schedule in command.weekly_schedule()
        ]

        class_entity = Class(
            ClassId(),
            subject = command.subject(),
            degree = command.degree(),
            section = command.section(),
            academic_period = command.academic_period(),
            schedule = Schedule(weekly_schedule)
        )

        self.__repository.save(class_entity)