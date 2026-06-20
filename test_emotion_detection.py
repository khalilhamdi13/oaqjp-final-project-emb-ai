import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_valid(self):
        result, status = emotion_detector("I am happy")
        self.assertEqual(status, 200)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_empty(self):
        result, status = emotion_detector("")
        self.assertEqual(status, 400)


if __name__ == "__main__":
    unittest.main()