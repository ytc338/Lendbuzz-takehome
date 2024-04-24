# word_count.py
from flask import jsonify, request
from init import init_app

app = init_app("word-count", "http://localhost:8082/count")

@app.route('/count', methods=['POST'])
def count_words():
    data = request.json
    text = data.get('text')
    word_count = len(text.split())
    return jsonify(word_count)


if __name__ == '__main__':
    app.run(port=8082, debug=True)
