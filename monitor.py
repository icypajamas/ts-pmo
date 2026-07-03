import psutil
import argparse
import time
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
args = parser.parse_args()

print("ts-pmo - v1.0")

if args.verbose:
    print("Hi hi hi")
    print(psutil.cpu_count())
else:
    print("Verbose mode is off. Use -v for more details.")

    print("======= CPU =======")
    print()
    print("======= Memory =======")                    

    while True:
        cpu_percent = psutil.cpu_percent()
        cpu_freq = psutil.cpu_freq()
        cpu_max = cpu_freq.max / 1000 if cpu_freq else 0
        cpu_min = cpu_freq.min / 1000 if cpu_freq else 0

        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        mem_total = mem.total / (1024**3)
        mem_avail = mem.available / (1024**3)

        # Move up 2 lines to CPU data
        print("\033[2F", end="", )
        print("\r\033[2K", end="", )
        print(f"CPU Usage: {cpu_percent}%  |  Max Clock: {cpu_max:.1f} GHz  |  Min Clock: {cpu_min:.1f} GHz", end="", )

        # Move down 2 lines to RAM data
        print("\033[2E", end="", )
        print("\r\033[2K", end="", )
        print(f"RAM Usage: {mem_percent}%  |  Total: {mem_total:.2f} GB  |  Available: {mem_avail:.2f} GB", end="", flush=True)

        time.sleep(1)