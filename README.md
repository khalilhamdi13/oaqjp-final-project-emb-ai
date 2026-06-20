# Emotion Detection App

This project is a Python-based web application that uses Natural Language Processing (NLP) to analyze text and detect human emotions such as joy, anger, sadness, fear, and disgust.

The application integrates IBM Watson NLP services to process user input and return structured emotional insights.

---

## Features

* Detects emotions from user input text
* Returns emotion scores (joy, anger, sadness, fear, disgust)
* Identifies the dominant emotion
* Web interface using Flask
* Unit tested for reliability
* Error handling for invalid inputs

---

## Technologies Used

* Python 3
* Flask
* IBM Watson NLP API
* unittest (for testing)
* pylint (for code quality)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/emotion-detector.git
   cd emotion-detector
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Run the Application

```bash
python server.py
```

Then open your browser and use:

```
http://localhost:5000/emotionDetector?text=I am happy
```

---

## Run Tests

```bash
python -m unittest test_emotion_detection.py
```

---

## Example Output

```json
{
  "joy": 0.90,
  "anger": 0.01,
  "sadness": 0.02,
  "fear": 0.03,
  "disgust": 0.01,
  "dominant_emotion": "joy"
}
```

---

## Project Structure

```
EmotionDetection/
│── __init__.py
│── emotion_detection.py
│
server.py
test_emotion_detection.py
README.md
```

---

## Author

Khalil HAMDI
