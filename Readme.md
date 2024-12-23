The script is working but there was a problem with my permisions to get the running containers from docker

# Dockerfile:

````# Use a Python base image
FROM python:3.11-slim

# Install git
RUN apt-get update && apt-get install -y git

# Create a working directory
WORKDIR /app

# Clone the GitHub repository (change to your repo URL)
RUN rm -rf /app/* && git clone https://github.com/Kugesz/Discord-Bot-Ip-Logger .

# Install dependencies from requirements.txt (if applicable)
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for your .env file
COPY .env .env

# Run the Python script
CMD ["python", "main.py"]```
````
