from src.Domain.Class.Class import Class
from src.Domain.Class.Contracts.ClassRepository import ClassRepository
from src.Domain.Class.ValueObjects.ClassId import ClassId


class MongoDbClassRepository(ClassRepository):
    def save(self, class_entity: Class):
        pass

    def find(self, class_id: ClassId) -> Class | None:
        pass

    def search(self, criteria: list) -> list[Class]:
        pass

    def delete(self, class_entity: Class) -> None:
        pass