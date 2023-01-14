from src.Services.EmotionRecognition.EmotionRecognitionResponse import EmotionRecognitionResponse


class EmotionRecognitionsResponse:

    def __init__(self, emotion_recognitions: list[EmotionRecognitionResponse]):
        self.__emotion_recognitions = emotion_recognitions

    def emotion_recognitions(self):
        return self.__emotion_recognitions