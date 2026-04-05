import requests
import json

def emotion_detector(text):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    if text == "":
        return "Please input text"

    PAYLOAD = { "raw_document": { "text": text}}
    response = requests.post(URL, json=PAYLOAD, headers=HEADERS)

    if response.status_code == 200:
        json_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
        sweet_emotion = max(list(json_response.values()))
        for emotion, score in json_response.items():
            if score == sweet_emotion:
                sweet_emotion = emotion
        json_response['dominant_emotion'] = sweet_emotion
        return json_response
    elif response.status_code == 400:
        return {'fear': None, 'anger': None, 'disgust': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
