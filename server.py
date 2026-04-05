from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

"""
This module starts the main server
to run the application
"""
application = Flask("Emotion Detection")

@application.route("/")
def index_page():
    """
    This function simply returns the index (main page)
    as a template
    """
    return render_template("index.html")

@application.route("/emotionDetector")
def emotion_detection():
    """
    This function returns the output of the
    emotion detector. If there is an error
    it retuns an invalid text error
    """
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)

    if type(response) == dict and response["dominant_emotion"] is not None:
        response_text = "For the given statement, the system response is {}. The dominant emotion is {}."
        all_pairs = ""
        for em, sc in response.items():
            if em is not "dominant_emotion":
                all_pairs += f"\'{em}\': {sc}, "

        all_pairs = all_pairs[0:-2]
        return response_text.format(all_pairs, response['dominant_emotion'])
    else:
        return "Invalid text! Please try again!"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)
