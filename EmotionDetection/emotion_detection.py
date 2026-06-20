import requests

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

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    payload = {
        "raw_document": {"text": text_to_analyze}
    }

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    emotions = data["emotionPredictions"][0]["emotion"]

    dominant = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant

    return emotions, 200