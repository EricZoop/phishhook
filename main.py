import nltk
nltk.download('stopwords')
nltk.download('punkt')

from flask import Flask, render_template, request, jsonify
import os
import pickle
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

# Define a preprocessing function for text
def preprocess_text(text):
    if pd.isnull(text):
        return ''
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    additional_stop_words = ['mailto', 'subject', 'from', 'to']
    stop_words.update(additional_stop_words)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Define the Flask app
app = Flask(__name__)

# Define Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['input_text']
    word_count = len(input_text.split())
    preprocessed_text = preprocess_text(input_text)

    # Load the saved pipeline
    with open('phish_hook_classifier.pkl', 'rb') as file:
        pipeline = pickle.load(file)

    # Make predictions using the loaded pipeline
    predicted_probabilities = pipeline.predict_proba([preprocessed_text])
    phishing_probability = predicted_probabilities[0][1]

    # Define background color gradients
    danger = 'radial-gradient(circle farthest-corner at 17.1% 22.8%, rgba(226,24,24,1) 0%, rgba(160,6,6,1) 90%)'
    scary = 'radial-gradient(circle farthest-corner at 10% 20%, rgba(242, 121, 1, 0.84) 20.8%, rgba(237, 3, 32, 0.87) 74.4%)'
    risky = 'linear-gradient( 91deg, rgba(72,154,78,1) 5.2%, rgba(251,206,70,1) 95.9% )'
    safe = 'radial-gradient( circle farthest-corner at 10% 20%, rgba(14,174,87,1) 0%, rgba(12,116,117,1) 90% )'
    default = 'linear-gradient(160deg, #0093E9 0%, #80D0C7 100%)'

    if phishing_probability >= 0.8 and word_count > 3:
        return jsonify({'result': f"{phishing_probability*100:.2f}% confident it is a phish", 'background_color': danger})
    elif phishing_probability >= 0.6 and word_count > 3:
        return jsonify({'result': f"{phishing_probability*100:.2f}% confident it is a phish", 'background_color': scary})
    elif phishing_probability >= 0.4 and word_count > 3:
        return jsonify({'result': f"{phishing_probability*100:.2f}% confident it is a phish", 'background_color': risky})
    elif phishing_probability >= 0.2 and word_count > 3:
        return jsonify({'result': f"{phishing_probability*100:.2f}% confident it is a phish", 'background_color': safe})
    elif phishing_probability < 0.2 and word_count > 3:
        return jsonify({'result': f"{phishing_probability*100:.2f}% confident it is a phish", 'background_color': default})
    else:
        return jsonify({'result': f"{0:.2f}% confident it is a phish", 'background_color': default})

if __name__ == '__main__':
    app.run(debug=True)