# Use a specific version of Alpine Linux as the base image
FROM alpine:3.15.3

# Use Python 3.11.6
ENV PYTHON_VERSION=3.11.6

# Install necessary system dependencies
RUN apk add --no-cache python${PYTHON_VERSION} py3-pip

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./app/requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire app directory into the container at /app
COPY ./app /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the FastAPI app using uvicorn
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
