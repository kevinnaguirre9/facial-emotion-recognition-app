from datetime import datetime

from src.Domain.Common.BaseEntity import BaseEntity
from src.Domain.EmotionRecognition.ValueObjects.Emotion import Emotion
from src.Domain.EmotionRecognition.ValueObjects.EmotionRecognitionId import EmotionRecognitionId
from src.Domain.Session.ValueObjects.SessionId import SessionId


class EmotionRecognition(BaseEntity):

    def __init__(
            self,
            emotion_recognition_id: EmotionRecognitionId,
            session_id: SessionId,
            angry: int,
            disgusted: int,
            fearful: int,
            happy: int,
            neutral: int,
            sad: int,
            surprised: int,
            recorded_at: datetime,
    ):
        super().__init__(emotion_recognition_id)
        self.__emotion_recognition_id = emotion_recognition_id
        self.__session_id = session_id
        self.__angry = angry
        self.__disgusted = disgusted
        self.__fearful = fearful
        self.__happy = happy
        self.__neutral = neutral
        self.__sad = sad
        self.__surprised = surprised
        self.__recorded_at = recorded_at


    @staticmethod
    def create(
            emotion_recognition_id: EmotionRecognitionId,
            session_id: SessionId,
            total_angry: int,
            total_disgusted: int,
            total_fearful: int,
            total_happy: int,
            total_neutral: int,
            total_sad: int,
            total_surprised: int,
            recorded_at: datetime = datetime.now(),
    ):
        return EmotionRecognition(
            emotion_recognition_id,
            session_id,
            total_angry,
            total_disgusted,
            total_fearful,
            total_happy,
            total_neutral,
            total_sad,
            total_surprised,
            recorded_at,
        )


    def emotion_recognition_id(self) -> EmotionRecognitionId:
        return self.__emotion_recognition_id

    def session_id(self) -> SessionId:
        return self.__session_id

    def recorded_at(self) -> datetime:
        return self.__recorded_at

    def total_angry(self) -> int:
        return self.__angry

    def total_disgusted(self) -> int:
        return self.__disgusted

    def total_fearful(self) -> int:
        return self.__fearful

    def total_happy(self) -> int:
        return self.__happy

    def total_neutral(self) -> int:
        return self.__neutral

    def total_sad(self) -> int:
        return self.__sad

    def total_surprised(self) -> int:
        return self.__surprised

    def to_primitives(self) -> dict:
        return {
            'emotion_recognition_id': self.emotion_recognition_id().value(),
            'session_id': self.session_id().value(),
            'angry': self.total_angry(),
            'disgusted': self.total_disgusted(),
            'fearful': self.total_fearful(),
            'happy': self.total_happy(),
            'neutral': self.total_neutral(),
            'sad': self.total_sad(),
            'surprised': self.total_surprised(),
            'recorded_at': self.recorded_at().isoformat(),
        }


    @classmethod
    def from_primitives(cls, emotion_recognition_data: dict) -> 'EmotionRecognition':
        return cls(
            EmotionRecognitionId(emotion_recognition_data['emotion_recognition_id']),
            SessionId(emotion_recognition_data['session_id']),
            emotion_recognition_data['angry'],
            emotion_recognition_data['disgusted'],
            emotion_recognition_data['fearful'],
            emotion_recognition_data['happy'],
            emotion_recognition_data['neutral'],
            emotion_recognition_data['sad'],
            emotion_recognition_data['surprised'],
            datetime.fromisoformat(emotion_recognition_data['recorded_at']),
        )
