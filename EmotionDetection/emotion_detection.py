import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # handle completely blank input locally
        return {'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None}

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 400:  # handle blank or invalid text sent to server
        return {'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None}

    response_dict = response.json()
    emotions = response_dict['emotionPredictions'][0]['emotion']
    scores = {k: emotions[k] for k in ['anger','disgust','fear','joy','sadness']}
    dominant_emotion = max(scores, key=scores.get)
    return {**scores,'dominant_emotion': dominant_emotion}
