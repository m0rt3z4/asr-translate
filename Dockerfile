# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install pip requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Expose port 8000 for the application
EXPOSE 8000

# Load environment variables from the .env file
COPY .env ./
ENV DOTENV_PATH=/usr/src/app/.env

# Run uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
