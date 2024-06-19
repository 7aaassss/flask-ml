FROM python:3.9-slim

LABEL authors="Art2m"

WORKDIR /app

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000


CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]