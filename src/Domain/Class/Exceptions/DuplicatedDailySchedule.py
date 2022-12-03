from src.Domain.Class.ValueObjects.Weekday import Weekday


class DuplicatedDailySchedule ( Exception ):
    def __init__ (self , weekday : Weekday ):
        super().__init__ (f'Duplicated daily schedule for weekday {weekday}')