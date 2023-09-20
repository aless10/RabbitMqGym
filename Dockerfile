# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts into the container
COPY . .

# Install the pika library for RabbitMQ
RUN pip install -r requirements.txt

# Expose any necessary ports (e.g., RabbitMQ)
EXPOSE 5672

