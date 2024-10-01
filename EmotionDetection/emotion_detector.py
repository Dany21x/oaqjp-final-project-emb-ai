import requests

def get_dominant_emotion(scores):
    return max(scores, key=scores.get)

def emotion_detector(text_to_analyze: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=data, timeout=10)

    if response.status_code == 400:
        return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    response_json = response.json()

    emotions_dict = response_json['emotionPredictions'][0]['emotion']
    emotions_dict['dominant_emotion'] = get_dominant_emotion(emotions_dict)

    return emotions_dict
