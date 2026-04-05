from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

application = Flask("Emotion Detection")

@application.route("/")
def index_page():
    return render_template("index.html")

@application.route("/emotionDetector")
def emotion_detection():
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)

    if (type(response) == str):
        return response
    
    if response["dominant_emotion"] is not None:
        response_text = "For the given statement, the system response is {}. The dominant emotion is {}."
        all_pairs = ""
        for em, sc in response.items():
            if em is not "dominant_emotion":
                all_pairs += f"\'{em}\': {sc}, "

        all_pairs = all_pairs[0:-2]
        return response_text.format(all_pairs, response['dominant_emotion'])
    
    return "Invalid text! Please try again!"
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)
