from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect():

    text = request.args.get("textToAnalyze")

    if not text or text.strip() == "":
        return "Invalid input", 400

    result, status = emotion_detector(text)

    if status == 400:
        return "Invalid input", 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
