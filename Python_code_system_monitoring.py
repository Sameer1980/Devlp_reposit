import psutil

# CPU Information
def cpu_info():
   print("CPU Cores:", psutil.cpu_count())
   print("CPU Utilization:", psutil.cpu_percent(interval=1), "%")

# Memory Information
def memory_info():
   memory = psutil.virtual_memory()
   print("Total Memory:", memory.total / 1024.0**3, "GB")
   print("Available Memory:", memory.available / 1024.0**3, "GB")
   print("Memory Utilization:", memory.percent, "%")

# Disk Information
def disk_info():
   disk = psutil.disk_usage('/')
   print("Total Disk:", disk.total / 1024.0**3, "GB")
   print("Used Disk:", disk.used / 1024.0**3, "GB")
   print("Disk Utilization:", disk.percent, "%")

# Heat Monitoring
def heat_info():
   temperatures = psutil.sensors_temperatures()
   if 'coretemp' in temperatures:
       for entry in temperatures['coretemp']:
           print(f"{entry.label} Temperature:", entry.current, "C")
   else:
       print("CPU Temperature data not available.")

# Call functions
cpu_info()
memory_info()
disk_info()
heat_info()
This