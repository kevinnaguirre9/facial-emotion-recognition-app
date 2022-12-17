from src.Domain.Common.Contracts.Query import Query


class SearchSessionsQuery(Query):

    def __init__(self, filters: dict, page: int, per_page: int):
        self.__filters = filters
        self.__page = page
        self.__per_page = per_page

    def filters(self) -> dict:
        return self.__filters

    def page(self) -> int:
        return self.__page

    def per_page(self) -> int:
        return self.__per_page