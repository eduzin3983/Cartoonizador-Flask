# Use the official Python image as a base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Install the system libraries required for OpenCV to work
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on (Flask default port)
EXPOSE 5000

# Set environment variables for Flask
# FLASK_APP specifies the entry point of the application
# FLASK_RUN_HOST allows the app to be accessible externally
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the Flask application
CMD ["flask", "run"]
