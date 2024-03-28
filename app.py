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
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('lrm.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['input_text']
    text = preprocess_text(input_text)
    X = vectorizer.transform([text])
    predictions = model.predict_proba(X)
    percentage = predictions[0][1] * 100
    return jsonify({'result': f"Probability of being a positive class (malicious mail): {percentage:.2f}%"})

if __name__ == '__main__':
    app.run(debug=True)