#!/usr/bin/python3

print('Hello world')
import psutil

#Get CPU usage (update every second)
cpu_percent = pstil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

# Get memory information
mem = psutil.virtual_memory()
print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
print(f"Used Memory: {mem.used / (1024**3):.2f} GB")
print(f"Memory Usage: {mem.percent}%")

#Get disk usage (for root directory)
disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024**3):.2f} GB")
print(f"Disk Usage: {disk.percent}%")



