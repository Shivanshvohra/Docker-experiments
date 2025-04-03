🐍 Python Logging Application with Docker
This project demonstrates how to create a Python application that logs data continuously to a file and runs inside a Docker container. The logs are stored in a Docker volume, ensuring persistence even after the container is stopped or removed.

📁 Project Structure
.
├── app.py            # Python application that generates logs
└── Dockerfile        # Dockerfile to build the image
📥 Prerequisites
Before starting, make sure you have Docker installed on your system:

Get Docker

🛠️ Steps to Build and Run the Application
🐍 Step 1: Write the Python Logging Application
Create a file named app.py with the following improved content:

import time
import os

LOG_FILE = "/data/app.log"
MAX_LOG_SIZE = 1 * 1024 * 1024  # 1MB

def rotate_logs():
    """Rename the log file if it exceeds MAX_LOG_SIZE."""
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) >= MAX_LOG_SIZE:
        os.rename(LOG_FILE, "/data/app.log.bak")

def log_message():
    """Log a formatted message to the log file and console."""
    message = f"[{time.ctime()}] - App is running\n"
    print(message, end="")  # Print to console

    with open(LOG_FILE, "a") as log_file:
        log_file.write(message)
        log_file.flush()  # Ensure immediate write to disk

if __name__ == "__main__":
    while True:
        rotate_logs()
        log_message()
        time.sleep(5)
🔧 Enhancements:
Uses RotatingFileHandler to manage log size and prevent unlimited growth.
Logs messages with timestamps, severity levels, and formatted output.
Logs to both the file (/data/app.log) and the console (stdout).
🛠️ Step 2: Create a Dockerfile
Create a file named Dockerfile with the following content:

# Use a minimal base Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/app.py

# Ensure the /data directory exists for logs
RUN mkdir -p /data

# Run the Python application
CMD ["python", "app.py"]
🔧 Enhancements:
Uses a lightweight Python 3.9-slim image to reduce container size.
Ensures /data directory exists for logging.
🚀 Step 3: Build the Docker Image
Run the following command to build the Docker image:

docker build -t python-log-app .
This creates an image named python-log-app.

🚀 Step 4: Run the Docker Container with a Persistent Volume
To ensure logs are persisted, mount a Docker volume when running the container:

docker run -d --name log-container -v my-app-data:/data python-log-app
Explanation:
-d : Runs the container in detached mode.
--name log-container : Assigns a name to the container.
-v my-app-data:/data : Mounts a Docker volume (my-app-data) to /data.
🧐 Step 5: Verify Logs
1️⃣ Check if the container is running:
docker ps
2️⃣ View real-time logs from the container:
docker logs -f log-container
3️⃣ Access the log file inside the container:
docker exec -it log-container sh
cd /data
cat app.log
4️⃣ Inspect the volume on the host system:
docker volume inspect my-app-data
🧹 Stopping and Cleaning Up
1️⃣ Stop the container:
docker stop log-container
2️⃣ Remove the container:
docker rm log-container
3️⃣ Remove the image (if needed):
docker rmi python-log-app
4️⃣ Remove the volume (if needed):
docker volume rm my-app-data
⚠️ Notes
The logs are stored persistently in the Docker volume my-app-data.
Log rotation prevents excessive log file growth.
You can modify the sleep interval or logging format as needed.