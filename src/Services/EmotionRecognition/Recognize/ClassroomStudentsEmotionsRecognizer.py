import cv2
import av
import numpy as np

from src.Domain.EmotionRecognition.ValueObjects.Emotion import Emotion
from src.Services.EmotionRecognition.Recognize.FaceEmotionRecognizer import FaceEmotionRecognizer
from src.Services.EmotionRecognition.Recognize.FacesDetector import FacesDetector
from src.Services.EmotionRecognition.Register.EmotionRecognitionRegister import EmotionRecognitionRegister
from src.Services.EmotionRecognition.Register.RegisterEmotionRecognitionCommand import RegisterEmotionRecognitionCommand


class ClassroomStudentsEmotionsRecognizer:

    def __init__(self):
        self.__faces_detector = FacesDetector()
        self.__face_emotion_recognizer = FaceEmotionRecognizer()
        self.__emotion_recognizer_register = EmotionRecognitionRegister()
        cv2.ocl.setUseOpenCL(False)



    def recognize(self, video_frame: av.VideoFrame) -> av.VideoFrame:

        video_frame = video_frame.to_ndarray(format="bgr24")

        gray_video_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)

        emotions_recognized_registry = {emotion.name: 0 for emotion in Emotion}

        faces = self.__faces_detector.detect(gray_video_frame)

        for (corner_x, corner_y, width, height) in faces:

            cv2.rectangle(
                image = video_frame,
                start_point = (corner_x, corner_y - 50),
                end_point = (corner_x + width, corner_y + height + 10),
                color = (255, 0, 0),
                thickness = 2
            )

            region_of_interest = gray_video_frame[corner_y:corner_y + height, corner_x:corner_x + width]

            face = np.expand_dims(
                np.expand_dims(cv2.resize(region_of_interest, (48, 48)), -1), 0
            )

            emotion_prediction = self.__face_emotion_recognizer.recognize(face)

            emotions_recognized_registry[emotion_prediction.name] += 1

            cv2.putText(
                image = video_frame,
                text = emotion_prediction.name,
                org = (corner_x + 20, corner_y - 60),
                font = cv2.FONT_HERSHEY_SIMPLEX,
                fontScale = 1,
                color = (255, 255, 255),
                thickness = 2,
                lineType = cv2.LINE_AA
            )

        self.__save_emotion_recognition('f630f8e7-5b9f-4ef9-afd2-72e85955735f', emotions_recognized_registry)

        return av.VideoFrame.from_ndarray(video_frame, format="bgr24")



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




