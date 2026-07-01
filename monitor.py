import psutil
import argparse
import time
import platform

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
# parser.add_argument()

args = parser.parse_args()

first = True


def cpuPrint():
    global first
    if first:
        print("======= CPU =======")
        first = False


def ramPrint():
    global first
    if first:
        print("======= Memory =======")
        first = False


print("ts-pmo 'This System Python Monitor' - v1.0")
if args.verbose:
    print("Hi hi hi")
    print(psutil.cpu_count())
else:
    print("Verbose mode is off. Use -v for more details.")
    while True:

        # CPU
        cpu_percent = psutil.cpu_percent()
        cpu_max = psutil.cpu_freq().max
        cpu_min = psutil.cpu_freq().min
        cpuPrint()
        print(
            f"\033[2K\rCPU Usage: {cpu_percent}%  |  Max Clock: {cpu_max/1000} GHz  |  Min Clock: {cpu_min/1000} GHz",
            end="",
            flush=True,
        )

        # RAM

        memory_percent = psutil.virtual_memory().percent
        memory_total = psutil.virtual_memory().total
        memory_free = psutil.virtual_memory().available
        ramPrint()
        print(
            f"\033[2K\rRAM Usage: {memory_percent}%  |  Total Memory: {memory_total/1000} GB  |  Available Memory: {memory_free/1000} GB",
            end="",
            flush=True,
        )
        time.sleep(1)
