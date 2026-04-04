from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.Test):
    def TestEmotion(self):
        result_one = emotion_detector("I am glad this happened")
        self.assertEqual(result_one["dominant_emotion"], "joy" )