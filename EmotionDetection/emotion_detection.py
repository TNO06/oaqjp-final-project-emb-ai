import requests
import json
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=payload)
    response_dict = response.json()
    emotions = response_dict['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    scores = {'anger': anger,'disgust': disgust,'fear': fear,'joy': joy,'sadness': sadness}
    dominant_emotion = max(scores, key=scores.get)
    return {'anger': anger,'disgust': disgust,'fear': fear,'joy': joy,'sadness': sadness,'dominant_emotion': dominant_emotion}
