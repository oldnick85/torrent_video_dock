FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    mediainfo \
    && rm -rf /var/lib/apt/lists/*

RUN pip install vcsi

COPY main.py /app/main.py
WORKDIR /app

CMD ["python3", "main.py", "--input-dir", "/app/data/input", "--output-dir", "/app/data/output"]