from flask import Flask
import requests


CENTRAL_MS_URL = "http://localhost:8080"


def init_app(service_name: str, service_url: str):
    """Initialize the core application."""
    app = Flask(service_name)

    with app.app_context():
        service_data = {
            "name": service_name,
            "url": service_url
        }
        requests.post(f"{CENTRAL_MS_URL}/services", json=service_data)

        return app
