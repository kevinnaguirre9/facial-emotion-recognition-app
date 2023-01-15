from abc import ABC, abstractmethod

from src.Domain.EmotionRecognition.EmotionRecognition import EmotionRecognition
from src.Domain.EmotionRecognition.ValueObjects.EmotionRecognitionId import EmotionRecognitionId


class EmotionRecognitionRepository(ABC):
    @abstractmethod
    def save(self, emotion_recognition_entity: EmotionRecognition):
        pass

    @abstractmethod
    def find(self, emotion_recognition_id: EmotionRecognitionId) -> EmotionRecognition|None:
        pass

    @abstractmethod
    def search(self, criteria: dict, limit: int|None, page: int|None) -> list[EmotionRecognition]|None:
        pass

    @abstractmethod
    def delete(self, emotion_recognition_entity: EmotionRecognition) -> None:
        pass