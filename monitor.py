import psutil
import time
from datetime import datetime
import os

# Create logs directory if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

log_file = "logs/system_log.txt"

def log_system_usage():
    with open(log_file, "a") as f:
        f.write("="*40 + "\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"CPU Usage: {psutil.cpu_percent()}%\n")
        f.write(f"Memory Usage: {psutil.virtual_memory().percent}%\n")
        f.write(f"Disk Usage: {psutil.disk_usage('/').percent}%\n")
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_hours = uptime_seconds / 3600
        f.write(f"System Uptime: {uptime_hours:.2f} hours\n")
        f.write("="*40 + "\n\n")

log_system_usage()
