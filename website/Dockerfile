FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Make sure Python sees /app
ENV PYTHONPATH=/app

EXPOSE 8000

# Run the app directly from app.py
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
