import requests
from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
from collections import Counter

app = Flask(__name__)


def get_word_frequency(url):
    # Fetch the web page content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text from the web page
    text = soup.get_text()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_frequency = Counter(words)

    # Convert the word frequency dictionary to JSON
    result = [{'word': word, 'frequency': freq} for word, freq in word_frequency.items()]

    return result

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template("index.html")


@app.route('/word-frequency', methods=['GET','POST'])
def word_frequency():
    # Get the URL from the request body
    url = request.json.get('url')

    # Call the function to get the word frequency
    result = get_word_frequency(url)

    # Return the result in JSON format
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
