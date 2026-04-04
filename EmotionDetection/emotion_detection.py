import requests
import json

def emotion_detector(text):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    if text == "":
        return "Please input text"

    PAYLOAD = { "raw_document": { "text": text}}
    response = json.loads(requests.post(URL, json=PAYLOAD, headers=HEADERS).text)['emotionPredictions'][0]['emotion']

    if response.status_code == 200:
        sweet_emotion = max(list(response.values()))

        for emotion, score in response.items():
            if score == sweet_emotion:
                sweet_emotion = emotion
        response["dominant_emotion"] = sweet_emotion
        return response
    