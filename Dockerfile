# Use a lightweight Python image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy Python script to the container
COPY scripts.py .

# Create directory structure
RUN mkdir -p /home/data/output

# Set the entry point to run the Python script
ENTRYPOINT ["python", "scripts.py"]
