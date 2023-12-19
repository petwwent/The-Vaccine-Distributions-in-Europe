# Use the official Python base image with Alpine Linux
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install the latest Flask version
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir Flask Werkzeug==2.0.3 uvicorn git

# Copy the entire project to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Python application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
