# Use a minimal base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the client script into the image
COPY client.py .

# Disable Python output buffering
ENV PYTHONUNBUFFERED=1

# Expose the port used by the client
EXPOSE 5000

# Command to run the client
CMD ["python", "client.py"]