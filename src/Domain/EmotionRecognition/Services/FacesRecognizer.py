from abc import ABC, abstractmethod

class FacesRecognizer(ABC):

    @abstractmethod
    def recognize(self, frame: list) -> list:
        pass