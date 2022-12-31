from src.Services.EmotionRecognition.Register.RegisterEmotionRecognitionCommand import RegisterEmotionRecognitionCommand
from src.Domain.EmotionRecognition.Contracts.EmotionRecognitionRepository import EmotionRecognitionRepository
from src.Domain.EmotionRecognition.EmotionRecognition import EmotionRecognition
from src.Domain.EmotionRecognition.ValueObjects.EmotionRecognitionId import EmotionRecognitionId
from src.Domain.Session.ValueObjects.SessionId import SessionId


class EmotionRecognitionRegister:

    def __init__(self, emotion_recognition_repository: EmotionRecognitionRepository):
        self.__emotion_recognition_repository = emotion_recognition_repository


    def handle(self, command: RegisterEmotionRecognitionCommand):

        session_id = SessionId(command.session_id())

        emotion_recognition = EmotionRecognition.create(
            EmotionRecognitionId(),
            session_id,
            command.total_angry(),
            command.total_disgusted(),
            command.total_fearful(),
            command.total_happy(),
            command.total_neutral(),
            command.total_sad(),
            command.total_surprised(),
        )

        self.__emotion_recognition_repository.save(emotion_recognition)