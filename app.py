from flask import Flask, request, render_template, jsonify
import re
import string
import pickle
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


# Function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(f'[{string.punctuation}]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    return text

# # Load the saved model and vectorizer
with open('fake_news_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)


# Function to predict if a new article is real or fake
def predict_news(title, text):
    combined = preprocess_text(title) + " " + preprocess_text(text)
    combined_tfidf = loaded_vectorizer.transform([combined])
    prediction = loaded_model.predict(combined_tfidf)
    return 'Real' if prediction[0] == 1 else 'Fake'


def scrap_news(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main heading (h1) and all paragraphs (p) on the page
        main_heading = soup.find('h1').text if soup.find('h1') else ''
        paragraphs = soup.find_all('p')

        # Extract the text content of all paragraphs
        article_content = ' '.join(paragraph.text for paragraph in paragraphs)

        return main_heading, article_content

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., invalid URL, no internet connection)
        print(f"An error occurred: {e}")
        return '', ''


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    new_title, new_text = scrap_news(url)
    if not new_title and not new_text:
        return jsonify({'error': 'Failed to extract news content'}), 500

    prediction = predict_news(new_title, new_text)
    return jsonify({'title': new_title, 'content': new_text, 'prediction': prediction})
@app.route('/predict_text' , methods=['POST'])
def predict_text():
    title = request.form.get('title')
    content = request.form.get('content')
    if not title:
        return jsonify({'error': 'Failed to extract news content'}), 500

    prediction = predict_news(title, content)
    return jsonify({'title': title, 'content': content, 'prediction': prediction})



if __name__ == '__main__':
    app.run(debug=True)
