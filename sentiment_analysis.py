# sentiment_analysis.py
from flask import jsonify, request
from textblob import TextBlob
from init import init_app

app = init_app("sentiment-analysis", "http://localhost:8081/analyze")


@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text')
    blob = TextBlob(text)
    sentiment = 'positive' if blob.sentiment.polarity > 0 else 'negative' if blob.sentiment.polarity < 0 else 'neutral'
    return jsonify(sentiment)


if __name__ == '__main__':
    app.run(port=8081, debug=True)
