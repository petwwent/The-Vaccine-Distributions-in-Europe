# Use the official Python base image with Alpine Linux
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install Flask directly in the Dockerfile
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir Flask==2.0.1 uvicorn

# Copy the entire project to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000
# Command to run the Python application using Uvicorn or relevant command for your app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
