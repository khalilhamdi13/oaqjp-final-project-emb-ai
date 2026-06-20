"""
Flask server for Emotion Detection Application
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def detect():
    """
    API endpoint to detect emotions from input text
    """
    text = request.args.get("textToAnalyze")

    if not text or text.strip() == "":
        return "Invalid input", 400

    result, status = emotion_detector(text)
    return jsonify(result), status


if __name__ == "__main__":
    app.run(debug=True)
