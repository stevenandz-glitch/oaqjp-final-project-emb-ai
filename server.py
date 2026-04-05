from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template

application = Flask("Emotion Detection")

@application.route("/")
def index_page():
    return render_template("index.html")

@application.route("/emotionDetector")
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
