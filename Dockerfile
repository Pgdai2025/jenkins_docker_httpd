# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy server script
COPY app.py .

# Expose the port
EXPOSE 8080

# Run the server
CMD ["python", "app.py"]
