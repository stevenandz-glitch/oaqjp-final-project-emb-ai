from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result_one = emotion_detector("I am glad this happened")
        self.assertEqual(result_one["dominant_emotion"], "joy" )

        result_two = emotion_detector("I am really mad about this")
        self.assertEqual(result_two["dominant_emotion"], "anger")

        result_three = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_three["dominant_emotion"], "disgust")

        result_four = emotion_detector("I am so sad about this")
        self.assertEqual(result_four["dominant_emotion"], "sadness")

        result_five = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_five["dominant_emotion"], "fear")

unittest.main()
