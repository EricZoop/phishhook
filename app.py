from flask import Flask, render_template, request, jsonify
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Define a preprocessing function for text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

app = Flask(__name__)

# Load the TF-IDF vectorizer and logistic regression model
with open('src/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)
with open('src/lrm.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['input_text']
    word_count = len(input_text.split())
    text = preprocess_text(input_text)
    X = vectorizer.transform([text])
    predictions = model.predict_proba(X)
    percentage = predictions[0][1] * 100

    # Define background color gradients
    danger = 'radial-gradient(circle farthest-corner at 17.1% 22.8%, rgba(226,24,24,1) 0%, rgba(160,6,6,1) 90%)'
    scary = 'radial-gradient(circle farthest-corner at 10% 20%, rgba(242, 121, 1, 0.84) 20.8%, rgba(237, 3, 32, 0.87) 74.4%)'
    risky = 'linear-gradient( 91deg, rgba(72,154,78,1) 5.2%, rgba(251,206,70,1) 95.9% )'
    safe = 'radial-gradient( circle farthest-corner at 10% 20%, rgba(14,174,87,1) 0%, rgba(12,116,117,1) 90% )'
    default = 'linear-gradient(160deg, #0093E9 0%, #80D0C7 100%)'

    if percentage >= 80 and word_count > 3:
        return jsonify({'result': f"{percentage:.2f}% confidence it is a phish", 'background_color': danger})
    elif percentage >= 60 and word_count > 3:
        return jsonify({'result': f"{percentage:.2f}% confidence it is a phish", 'background_color': scary})
    elif percentage >= 40 and word_count > 3:
        return jsonify({'result': f"{percentage:.2f}% confidence it is a phish", 'background_color': risky})
    elif percentage >= 20 and word_count > 3:
        return jsonify({'result': f"{percentage:.2f}% confidence it is a phish", 'background_color': safe})
    elif percentage < 20 and word_count > 3:
        return jsonify({'result': f"{percentage:.2f}% confidence it is a phish", 'background_color': default})
    else:
        return jsonify({'result': f"{0:.2f}% confidence it is a phish", 'background_color': default})


if __name__ == '__main__':
    app.run(debug=True)
