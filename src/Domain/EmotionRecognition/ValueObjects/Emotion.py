from enum import Enum


class Emotion(Enum):
    ANGRY = 0
    DISGUSTED = 1
    FEARFUL = 2
    HAPPY = 3
    NEUTRAL = 4
    SAD = 5
    SURPRISED = 6

    @staticmethod
    def from_name(emotion: str) -> 'Emotion':
        return Emotion[emotion.upper()]
