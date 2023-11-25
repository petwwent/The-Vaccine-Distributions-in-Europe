# Use a specific version of Alpine Linux as the base image
FROM alpine:3.15.3

# Use Python 3.11.6
ENV PYTHON_VERSION=3.11.6

# Install necessary system dependencies
RUN apk add --no-cache python${PYTHON_VERSION} py3-pip

# Set the working directory in the container
WORKDIR /app

# Copy the requirements directory into the container at /app/requirements
COPY requirements /app/requirements

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements/requirements.txt

# Copy the rest of the files into the container
COPY . .

# Expose the port that the FastAPI app will run on
EXPOSE 5000

# Command to run the FastAPI app using uvicorn
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
