# Use an official Python runtime as a base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy only requirements to cache them in Docker layer
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps gcc libc-dev linux-headers

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Run the app with uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
