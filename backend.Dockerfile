FROM python:3.7-slim

WORKDIR /file_sharing
COPY requirements.txt .

RUN apt-get update \
&& pip install -r requirements.txt \
&& rm -rf /var/lib/apt/lists/*

COPY . .

# ENTRYPOINT ["python3.7", "wsgi.py"]