FROM python:3.9-slim-buster

# Copy the application directory to the container
COPY . /app

# Set the working directory to the app directory
WORKDIR /app

# Install dependencies
RUN apt-get update && \
   apt-get install -y build-essential && \
   pip install --upgrade pip && \
   pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]