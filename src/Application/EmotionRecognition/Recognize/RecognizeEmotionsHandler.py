from datetime import datetime

from src.Application.EmotionRecognition.Recognize.RecognizeEmotionsCommand import RecognizeEmotionsCommand
from src.Domain.Common.Contracts.CommandHandler import CommandHandler
from src.Domain.EmotionRecognition.Contracts.EmotionRecognitionRepository import EmotionRecognitionRepository
from src.Domain.EmotionRecognition.EmotionRecognition import EmotionRecognition
from src.Domain.EmotionRecognition.Services.EmotionRecognizer import EmotionRecognizer
from src.Domain.EmotionRecognition.Services.FacesRecognizer import FacesRecognizer
from src.Domain.EmotionRecognition.ValueObjects.EmotionRecognitionId import EmotionRecognitionId
from src.Domain.Session.ValueObjects.SessionId import SessionId


class RecognizeEmotionsHandler(CommandHandler):

    def __init__(
            self,
            emotion_recognition_repository: EmotionRecognitionRepository,
            faces_recognizer: FacesRecognizer,
            emotion_recognizer: EmotionRecognizer,
    ):
        self.__emotion_recognition_repository = emotion_recognition_repository
        self.__faces_recognizer = faces_recognizer
        self.__emotion_recognizer = emotion_recognizer


    def handle(self, command: RecognizeEmotionsCommand):

        frame = command.frame()

        session_id = SessionId(command.session_id())

        recorded_time = datetime.now()

        faces = self.__faces_recognizer.recognize(frame)

        emotions_recognized = list(map(self.__emotion_recognizer.recognize, faces))

        #Get total students matching each recognized emotion
        emotions_recognized_count = dict(
            (emotion, emotions_recognized.count(emotion))
            for emotion in set(emotions_recognized)
        )

        #Save the records!
        for emotion, total_students in emotions_recognized_count.items():

            emotion_recognition = EmotionRecognition.create(
                EmotionRecognitionId(),
                session_id,
                emotion,
                total_students,
                recorded_time
            )

            self.__emotion_recognition_repository.save(emotion_recognition)

        #todo: return frame with emotions recognized in each face