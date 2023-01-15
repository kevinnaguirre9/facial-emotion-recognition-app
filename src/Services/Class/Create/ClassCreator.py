from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Services.Class.Create import CreateClassCommand
from src.Domain.Class.Class import Class
from src.Domain.Class.Contracts.ClassRepository import ClassRepository


class ClassCreator:

    def __init__(self, repository: ClassRepository):
        self.__repository = repository


    def handle(self, command: CreateClassCommand):

        class_entity = Class.create(
            ClassId(),
            subject = command.subject(),
            degree = command.degree(),
            section = command.section(),
            academic_period = command.academic_period(),
        )

        self.__repository.save(class_entity)