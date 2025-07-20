# Use official TensorFlow image as base
FROM tensorflow/tensorflow:2.13.0

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python dependencies
RUN pip install Flask gunicorn Pillow keras_preprocessing

# Expose port
EXPOSE 8000

# Run your Flask app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
