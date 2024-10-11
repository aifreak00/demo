# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
