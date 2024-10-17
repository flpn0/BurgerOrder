FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000
ENV PYTHONUNBUFFERED="yes"

ENTRYPOINT ["python3", "app.py"]