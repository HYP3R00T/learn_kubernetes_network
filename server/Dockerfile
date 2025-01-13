# Use a minimal base image
FROM python:3.9-slim

# Copy server code
WORKDIR /app
COPY server.py .

# Run the server
CMD ["python", "server.py"]