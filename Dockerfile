# Use the Python 3.9 image from the Alpine repository as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to the container at /app
COPY . .

# Set environment variables
ENV FLASK_APP=main.py  # Change this to your main Python file
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "run"]
