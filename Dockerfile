FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev postgresql-client

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN python3 manage.py collectstatic --no-input

RUN python3 manage.py makemigrations
