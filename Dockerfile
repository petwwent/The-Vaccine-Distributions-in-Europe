# Use the Python 3.9 image from the Alpine repository as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the main.py file from its directory to the working directory
COPY main.py /app

# Create a directory named 'data' in the working directory and copy data.json into it
COPY json-Europe-SelectedColumns.json /data

# Install any necessary dependencies
RUN pip install flask  #  API is built using Flask

# Expose the port your API will run on
EXPOSE 5000

# Define the command to run your application (API)
CMD ["python", "main.py"]
