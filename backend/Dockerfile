# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=10000

# Install system dependencies
# We NEED git for the application to clone repositories
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose the port the app runs on
EXPOSE 10000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "2", "--timeout", "120", "run_api:app"]
