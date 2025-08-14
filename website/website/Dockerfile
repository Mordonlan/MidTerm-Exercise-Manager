FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the whole project into the container
COPY . .

# Expose port 8000 to the outside
EXPOSE 8000

# Run the Flask app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "website.app:app"]
