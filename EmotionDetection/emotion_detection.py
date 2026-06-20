import requests

def emotion_detector(text_to_analyze):
# Handle empty input
if text_to_analyze is None or text_to_analyze.strip() == "":
return None

```
# Mock response (simulating Watson NLP API)
emotions = {
    "anger": 0.1,
    "disgust": 0.05,
    "fear": 0.2,
    "joy": 0.6,
    "sadness": 0.05
}

dominant_emotion = max(emotions, key=emotions.get)
emotions["dominant_emotion"] = dominant_emotion

return emotions
```
