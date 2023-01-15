
class SearchEmotionRecognitionsQuery:

    def __init__(self, filters: dict, page: int|None = None, per_page: int|None = None):
        self.__filters = filters
        self.__page = page
        self.__per_page = per_page

    def filters(self) -> dict:
        return self.__filters

    def page(self) -> int|None:
        return self.__page

    def per_page(self) -> int|None:
        return self.__per_page