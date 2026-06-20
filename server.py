"""
Flask server for Emotion Detection Application
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Endpoint for emotion detection
    """

    text = request.args.get("textToAnalyze")

    result, status = emotion_detector(text)

    if status == 400:
        return {"error": "Invalid input"}, 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
