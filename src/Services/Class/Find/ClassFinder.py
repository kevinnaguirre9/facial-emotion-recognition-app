from src.Domain.Class.Contracts.ClassRepository import ClassRepository
from src.Domain.Class.Exceptions.ClassNotFound import ClassNotFound
from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Services.Class.ClassResponse import ClassResponse
from src.Services.Class.Find.FindClassQuery import FindClassQuery


class ClassFinder:

    def __init__(self, repository: ClassRepository):
        self.__repository = repository

    def handle(self, query: FindClassQuery) -> ClassResponse|None:

        class_entity = self.__repository.find(ClassId(query.class_id()))

        if class_entity is None:
            raise ClassNotFound()

        return ClassResponse(
            class_entity.class_id().value(),
            class_entity.subject(),
            class_entity.degree(),
            class_entity.section(),
            class_entity.academic_period(),
        )