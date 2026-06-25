import psutil

print("Memory: ", psutil.virtual_memory().percent, "%")
print("CPU Frequency (Min):", psutil.cpu_freq().min / 1000, "GHz")
print("CPU Frequency (Max):", psutil.cpu_freq().max / 1000, "GHz")
print("CPU Frequency:", round(psutil.cpu_freq().current / 1000, 2), "GHz")
