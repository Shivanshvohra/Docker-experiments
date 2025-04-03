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