import cv2
import av
import numpy as np

from src.Domain.EmotionRecognition.Contracts.EmotionRecognitionRepository import EmotionRecognitionRepository
from src.Domain.EmotionRecognition.ValueObjects.Emotion import Emotion
from src.Services.EmotionRecognition.Recognize.FaceEmotionRecognizer import FaceEmotionRecognizer
from src.Services.EmotionRecognition.Recognize.FacesDetector import FacesDetector
from src.Services.EmotionRecognition.Register.EmotionRecognitionRegister import EmotionRecognitionRegister
from src.Services.EmotionRecognition.Register.RegisterEmotionRecognitionCommand import RegisterEmotionRecognitionCommand


class ClassroomStudentsEmotionsRecognizer:

    def __init__(
            self,
            emotion_recognition_repository: EmotionRecognitionRepository,
            session_id: str,
    ):
        self.__session_id = session_id
        self.__faces_detector = FacesDetector()
        self.__face_emotion_recognizer = FaceEmotionRecognizer()
        self.__emotion_recognizer_register = EmotionRecognitionRegister(emotion_recognition_repository)
        cv2.ocl.setUseOpenCL(False)



    def recognize(self, video_frame: av.VideoFrame) -> av.VideoFrame:

        print(f"Recognizing emotions for session: {self.__session_id}")

        ndarray_video_frame = video_frame.to_ndarray(format="bgr24")

        gray_video_frame = cv2.cvtColor(ndarray_video_frame, cv2.COLOR_BGR2GRAY)

        emotions_recognized_registry = {emotion.name: 0 for emotion in Emotion}

        faces = self.__faces_detector.detect(gray_video_frame)

        if not np.any(faces):
            return video_frame

        for (corner_x, corner_y, width, height) in faces:

            cv2.rectangle(
                ndarray_video_frame,
                (corner_x, corner_y - 50),
                (corner_x + width, corner_y + height + 10),
                (255, 0, 0),
                2
            )

            region_of_interest = gray_video_frame[corner_y:corner_y + height, corner_x:corner_x + width]

            face = np.expand_dims(
                np.expand_dims(cv2.resize(region_of_interest, (48, 48)), -1), 0
            )

            emotion_prediction = self.__face_emotion_recognizer.recognize(face)

            emotions_recognized_registry[emotion_prediction.name] += 1

            cv2.putText(
                ndarray_video_frame,
                emotion_prediction.name,
                (corner_x + 20, corner_y - 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
                cv2.LINE_AA
            )

        self.__save_emotion_recognition(self.__session_id, emotions_recognized_registry)

        return av.VideoFrame.from_ndarray(ndarray_video_frame, format="bgr24")



    def __save_emotion_recognition(self, session_id: str, emotions_registry: dict):

        command = RegisterEmotionRecognitionCommand(
            session_id = session_id,
            total_angry = emotions_registry.get(Emotion.ANGRY.name),
            total_disgusted = emotions_registry.get(Emotion.DISGUSTED.name),
            total_fearful = emotions_registry.get(Emotion.FEARFUL.name),
            total_happy = emotions_registry.get(Emotion.HAPPY.name),
            total_neutral = emotions_registry.get(Emotion.NEUTRAL.name),
            total_sad = emotions_registry.get(Emotion.SAD.name),
            total_surprised = emotions_registry.get(Emotion.SURPRISED.name)
        )

        self.__emotion_recognizer_register.register(command)




