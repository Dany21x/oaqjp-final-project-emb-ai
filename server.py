"""
Emotion Detection Flask Application

This Flask-based web server provides an interface for detecting emotions from user input text.
The server includes an index page that serves as the main entry point and a POST endpoint
('/emotionDetector') that processes text and returns the detected emotions, including the
dominant emotion, through a pre-trained emotion detection model.

Routes:
    - '/' : Renders the index.html homepage.
    - '/emotionDetector' (POST): Accepts JSON input with a text field, analyzes the emotion
      using the emotion detection model, and returns the result.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    This function renders the 'index.html' template, which serves as the main page
    for the web application.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    This function receives a POST request containing a JSON object with the user's text.
    It uses a WATSON (IBM) emotion detection model to analyze the text and return a response.
    If the model cannot determine a dominant emotion, an error message is returned.
    """
    data = request.get_json()
    text_to_analyze = data['text']

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return jsonify({'error': ' Invalid text! Please try again!'}), 400

    formatted_dict = ', '.join(
        f'{key}: {value}' for key, value in response.items()
        if key != 'dominant_emotion'
    )

    formatted_response = f'''
        For the given statement, the system response is {formatted_dict}. 
        The dominant emotion is {response['dominant_emotion']}.
    '''

    return formatted_response

if __name__ == "__main__":
    app.run(debug=True)
