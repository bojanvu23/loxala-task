FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Use the startup script
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 