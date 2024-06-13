#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Download NLTK resources
python src/nlp_utils.py

# Run the main script
python src/main.py
