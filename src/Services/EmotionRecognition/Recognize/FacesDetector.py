import cv2
from numpy import ndarray


class FacesDetector:

    DEFAULT_SCALE_FACTOR = 1.3

    DEFAULT_MIN_NEIGHBORS = 5

    def __init__(self, scale_factor: float|None = None, min_neighbors: int|None = None):
        self.__load_haar_cascade_face_detector()
        self.__scale_factor = scale_factor or self.DEFAULT_SCALE_FACTOR
        self.__min_neighbors = min_neighbors or self.DEFAULT_MIN_NEIGHBORS

    def detect(self, gray_frame: ndarray) -> ndarray:
        return self.__face_cascade_classifier.detectMultiScale(
            gray_frame,
            self.__scale_factor,
            self.__min_neighbors
        )

    def __load_haar_cascade_face_detector(self):
        self.__face_cascade_classifier = cv2\
            .CascadeClassifier('neural-network/model/haarcascade_frontalface_default.xml')