from src.Domain.Common.Uuid import Uuid


class BaseEntity:
    def __init__(self, uuid: Uuid):
        self.__uuid = uuid

    def __str__(self) -> str:
        return str(self.__uuid)

    def __eq__(self, other: 'BaseEntity') -> bool:
        return self.__uuid == other.__uuid