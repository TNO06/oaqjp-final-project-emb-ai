"""
server.py

Flask server to detect emotions from user text using the EmotionDetection package.
Provides web interface and API endpoint.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """
    Handle emotion detection requests.
    Accepts POST requests with JSON containing 'text' key or
    GET requests with 'textToAnalyze' query parameter.
    Returns formatted response or error message for blank input.
    """
    if request.method == "POST":
        data = request.get_json()
        text_to_analyze = data.get("text", "")
    else:
        text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response


@app.route("/")
def index():
    """
    Serve the index.html template for user interface.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
