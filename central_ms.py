# central_ms.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
services = {}


@app.route('/services', methods=['POST'])
def add_service():
    service_data = request.json
    services[service_data['name']] = service_data['url']
    return jsonify({'message': 'Service registered successfully'}), 200


@app.route('/services', methods=['GET'])
def list_services():
    return jsonify(list(services.items())), 200


@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json
    service_name = data.get('service')
    text = data.get('text')

    if service_name not in services:
        return jsonify({'error': 'Requested service does not exist'}), 404

    service_url = services[service_name]
    response = requests.post(service_url, json={'text': text})

    if response.status_code == 200:
        return jsonify({'result': response.json()}), 200
    else:
        return jsonify({'error': 'Service error'}), 500


if __name__ == '__main__':
    app.run(port=8080, debug=True)
