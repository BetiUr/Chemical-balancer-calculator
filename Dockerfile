# Use an official lightweight Python image as the base
FROM python:3.11-slim

# Set a working directory inside the container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Metadata about the maintainer
LABEL maintainer="Beatrice Urbaite <beatrice.urbaite@mif.stud.vu.lt>"

# Command to run your Python app
CMD ["python", "Calculator_code.py"]