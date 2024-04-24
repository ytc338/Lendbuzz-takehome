#!/bin/bash

source bin/activate &

# Run Central Microservice
python3 central_ms.py &

# Run Sentiment Analysis Service
python3 sentiment_analysis.py &

# Run Word Count Service
python3 word_count.py &

# Run Entity Recognition Service
python3 entity_recognition.py &
