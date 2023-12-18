# Use the official Python base image with Alpine Linux
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Python application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
