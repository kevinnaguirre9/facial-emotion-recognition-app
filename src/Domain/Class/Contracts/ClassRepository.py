from abc import ABC, abstractmethod

from src.Domain.Class.Class import Class
from src.Domain.Class.ValueObjects.ClassId import ClassId


class ClassRepository(ABC):
    @abstractmethod
    def save(self, class_entity: Class):
        pass

    @abstractmethod
    def find(self, class_id: ClassId) -> Class|None:
        pass

    @abstractmethod
    def search(self, criteria: dict, limit: int, page: int) -> list[Class]|None:
        pass

    @abstractmethod
    def delete(self, class_entity: Class) -> None:
        pass

