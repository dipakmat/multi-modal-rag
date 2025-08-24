# Base image
FROM python:3.10-slim

# Set environment
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV APP_HOME=/app

WORKDIR $APP_HOME

# Install system dependencies (for OCR, PDFs)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose app port (if running as API later)
EXPOSE 8000

# Default command
CMD ["python", "main.py"]

# Run as API instead of CLI
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
