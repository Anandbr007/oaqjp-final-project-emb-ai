import json
import unittest

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_returns_emotion_scores(self):
        result = emotion_detector("I am really mad about this")
        data = json.loads(result)
        emotions = data["emotionPredictions"][0]["emotion"]

        for name in ["anger", "disgust", "fear", "joy", "sadness"]:
            self.assertIn(name, emotions)

    def test_anger_is_strongest_for_angry_text(self):
        result = emotion_detector("I am really mad about this")
        emotions = json.loads(result)["emotionPredictions"][0]["emotion"]

        self.assertEqual(max(emotions, key=emotions.get), "anger")


if __name__ == "__main__":
    unittest.main()