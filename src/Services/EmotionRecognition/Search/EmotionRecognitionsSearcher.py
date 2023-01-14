from collections.abc import Callable

from src.Domain.EmotionRecognition.Contracts.EmotionRecognitionRepository import EmotionRecognitionRepository
from src.Domain.EmotionRecognition.EmotionRecognition import EmotionRecognition
from src.Services.EmotionRecognition.EmotionRecognitionResponse import EmotionRecognitionResponse
from src.Services.EmotionRecognition.EmotionRecognitionsResponse import EmotionRecognitionsResponse
from src.Services.EmotionRecognition.Search import SearchEmotionRecognitionsQuery


class EmotionRecognitionsSearcher:

    def __init__(self, emotion_recognitions_repository: EmotionRecognitionRepository):
        self.emotion_recognitions_repository = emotion_recognitions_repository


    def handle(self, query: SearchEmotionRecognitionsQuery) -> EmotionRecognitionsResponse:
        emotion_recognitions = self.emotion_recognitions_repository.search(
            query.filters(), query.per_page(), query.page()
        )

        return EmotionRecognitionsResponse(
            list(map(self.to_response(), emotion_recognitions))
        )


    @classmethod
    def to_response(cls) -> Callable[[EmotionRecognition], EmotionRecognitionResponse]:
        return lambda emotion_recognition_entity: EmotionRecognitionResponse(
            emotion_recognition_entity.emotion_recognition_id().value(),
            emotion_recognition_entity.session_id().value(),
            emotion_recognition_entity.total_angry(),
            emotion_recognition_entity.total_disgusted(),
            emotion_recognition_entity.total_fearful(),
            emotion_recognition_entity.total_happy(),
            emotion_recognition_entity.total_neutral(),
            emotion_recognition_entity.total_sad(),
            emotion_recognition_entity.total_surprised(),
            emotion_recognition_entity.recorded_at().strftime('%Y-%m-%d %H:%M:%S'),
        )