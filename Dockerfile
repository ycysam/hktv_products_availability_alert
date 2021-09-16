FROM python:3.9.7-slim

WORKDIR /var/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt