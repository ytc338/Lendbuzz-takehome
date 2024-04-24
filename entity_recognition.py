# entity_recognition.py
import requests
from flask import jsonify, request
import spacy
from init import init_app

app = init_app("entity-recognition", "http://localhost:8083/recognize")
nlp = spacy.load("en_core_web_sm")


# Flag to track if registration is done
registration_done = False


@app.route('/recognize', methods=['POST'])
def recognize_entities():
    data = request.json
    text = data.get('text')
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    return jsonify(entities)


if __name__ == '__main__':
    app.run(port=8083, debug=True)
