# Use Alpine Linux as the base image
FROM python:3.9-alpine

# Install necessary build tools and dependencies
RUN apk update && \
    apk add --no-cache \
    build-base \
    autoconf \
    automake \
    libtool \
    cmake \
    ninja

# Install required Python packages, including 'numpy==1.26.2', and other packages
RUN pip install --no-cache-dir \
    fastapi==0.104.1 \
    numpy==1.26.2 \
    uvicorn==0.15.0 \
    pandas==1.3.3 \
    plotly==5.3.1


# Copy the rest of the files into the container
COPY . .

# Expose the port that the FastAPI app will run on
EXPOSE 5000

# Command to run the FastAPI app using uvicorn
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
