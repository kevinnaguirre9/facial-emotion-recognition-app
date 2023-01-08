from collections.abc import Callable

from src.Services.Class.ClassResponse import ClassResponse
from src.Services.Class.ClassesResponse import ClassesResponse
from src.Services.Class.Search.SearchClassesQuery import SearchClassesQuery
from src.Domain.Class.Class import Class
from src.Domain.Class.Contracts.ClassRepository import ClassRepository


class ClassesSearcher:

    def __init__(self, repository: ClassRepository):
        self.__repository = repository

    def handle(self, query: SearchClassesQuery) -> ClassesResponse:
        classes = self.__repository.search(
            query.filters(),
            query.per_page(),
            query.page()
        )

        return ClassesResponse(
            list(map(self.to_response(), classes))
        )

    @classmethod
    def to_response(cls) -> Callable[[Class], ClassResponse]:
        return lambda class_entity: ClassResponse(
            class_entity.class_id().value(),
            class_entity.subject(),
            class_entity.degree(),
            class_entity.section(),
            class_entity.academic_period(),
            class_entity.schedule().to_primitives(),
        )