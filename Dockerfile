FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py loaddata fixtures.json


CMD ["gunicorn", "it_bel_project.wsgi:application", "--bind", "0:8000" ]