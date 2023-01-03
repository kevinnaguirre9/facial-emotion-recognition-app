import os

import numpy as np
from keras.models import model_from_json
from numpy import ndarray

from src.Domain.EmotionRecognition.ValueObjects.Emotion import Emotion


class FaceEmotionRecognizer:
    def __init__(self):
        self.__emotion_model = self.__load_model()
        self.__emotions = {emotion.value: emotion.name for emotion in Emotion}

    def recognize(self, face: ndarray) -> Emotion:

        predictions = self.__emotion_model.predict(face)

        max_score_index = int(np.argmax(predictions))

        return Emotion.from_name(self.__emotions.get(max_score_index))

    @classmethod
    def __load_model(cls):
        emotion_model_json_file = open('neural-network/model/emotion_model.json', 'r')

        loaded_emotion_model = emotion_model_json_file.read()

        emotion_model_json_file.close()

        emotion_model = model_from_json(loaded_emotion_model)

        emotion_model.load_weights('neural-network/model/emotion_model.h5')

        return emotion_model