from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(**name**)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
text = request.args.get('text')

```
# Handle empty input
if not text:
    return jsonify({"message": "Invalid input! Please enter some text."}), 400

result = emotion_detector(text)

# Handle API error
if result is None:
    return jsonify({"message": "Error processing the request"}), 400

return jsonify(result)
```

if **name** == "**main**":
app.run(debug=True)
