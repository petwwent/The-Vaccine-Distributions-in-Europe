# Use the Python 3.9 image from the Alpine repository as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install required dependencies
RUN pip install -r requirements.txt

# Copy all files from the current directory to the container at /app
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "main.py"]
