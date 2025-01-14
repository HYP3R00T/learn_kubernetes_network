# Use a minimal base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the server script into the image
COPY server.py .

# Disable Python output buffering
ENV PYTHONUNBUFFERED=1

# Expose the port used by the server
EXPOSE 5000

# Command to run the server
CMD ["python", "server.py"]