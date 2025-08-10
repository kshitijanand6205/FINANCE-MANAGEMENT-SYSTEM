#!/usr/bin/env bash
set -o errexit

# Ensure script uses Unix line endings (LF) — IMPORTANT for Linux/Docker
# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
