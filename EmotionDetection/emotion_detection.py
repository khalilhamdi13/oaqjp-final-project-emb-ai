def emotion_detector(text_to_analyze):

    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }, 400

    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.2,
        "joy": 0.6,
        "sadness": 0.05
    }

    dominant = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant

    return emotions, 200