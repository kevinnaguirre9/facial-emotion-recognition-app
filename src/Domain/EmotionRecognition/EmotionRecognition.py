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
            emotion: Emotion,
            total_students: int,
            recorded_at: datetime,
    ):
        super().__init__(emotion_recognition_id)
        self._emotion_recognition_id = emotion_recognition_id
        self._session_id = session_id
        self._emotion = emotion
        self._total_students = total_students
        self._recorded_at = recorded_at


    @staticmethod
    def create(
            emotion_recognition_id: EmotionRecognitionId,
            session_id: SessionId,
            emotion: Emotion,
            total_students: int,
            recorded_at: datetime,
    ):
        return EmotionRecognition(
            emotion_recognition_id,
            session_id,
            emotion,
            total_students,
            recorded_at,
        )


    def emotion_recognition_id(self) -> EmotionRecognitionId:
        return self._emotion_recognition_id


    def session_id(self) -> SessionId:
        return self._session_id


    def emotion(self) -> Emotion:
        return self._emotion


    def total_students(self) -> int:
        return self._total_students


    def recorded_at(self) -> datetime:
        return self._recorded_at


    def to_primitives(self) -> dict:
        return {
            'emotion_recognition_id': self.emotion_recognition_id().value(),
            'session_id': self.session_id().value(),
            'emotion': self.emotion().value(),
            'total_students': self.total_students(),
            'recorded_at': self.recorded_at().isoformat(),
        }


    @classmethod
    def from_primitives(cls, emotion_recognition_data: dict) -> 'EmotionRecognition':
        return cls(
            EmotionRecognitionId(emotion_recognition_data['emotion_recognition_id']),
            SessionId(emotion_recognition_data['session_id']),
            Emotion(emotion_recognition_data['emotion']),
            emotion_recognition_data['total_students'],
            datetime.fromisoformat(emotion_recognition_data['recorded_at']),
        )
