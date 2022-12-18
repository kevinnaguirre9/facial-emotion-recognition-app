from abc import ABC, abstractmethod

from src.Domain.EmotionRecognition.ValueObjects.Emotion import Emotion


class EmotionRecognizer(ABC):

    @abstractmethod
    def recognize(self, face: list) -> Emotion:
        pass