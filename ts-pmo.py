import psutil
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
parser.add_argument(
    "-i", "--interval", type=int, default=1, help="Update interval in seconds"
)
parser.add_argument("--cpu-threshold", type=int, help="CPU usage threshold percentage")
parser.add_argument(
    "--mem-threshold", type=int, help="Memory usage threshold percentage"
)
args = parser.parse_args()

print("ts-pmo - v1.0")
interval = args.interval

if args.cpu_threshold or args.mem_threshold is not None:
    if args.verbose:
        with open("log.txt", "w") as file:
            print(
                "Threshold: CPU Usage > {}%".format(args.cpu_threshold)
                if args.cpu_threshold
                else ""
            )
            print(
                (
                    "Threshold: Memory Usage > {}%".format(args.mem_threshold)
                    if args.mem_threshold
                    else ""
                ),
                end="",
            )
            print()
            file.write(
                "Threshold: CPU Usage > {}%\n".format(args.cpu_threshold)
                if args.cpu_threshold
                else ""
            )
            file.write(
                "Threshold: Memory Usage > {}%\n".format(args.mem_threshold)
                if args.mem_threshold
                else ""
            )
            file.write("\n")
            file.write("Verbose Mode On\n")
            file.write("\n")
            file.write(
                "Timestamp, CPU Usage, Memory Usage, Packets Sent (K), Packets Received (K)\n"
            )
            file.write("\n")
    else:
        with open("log.txt", "w") as file:
            print(
                "Threshold: CPU Usage > {}%".format(args.cpu_threshold)
                if args.cpu_threshold
                else ""
            )
            print(
                (
                    "Threshold: Memory Usage > {}%".format(args.mem_threshold)
                    if args.mem_threshold
                    else ""
                ),
                end="",
            )
            print()
            file.write(
                "Threshold: CPU Usage > {}%\n".format(args.cpu_threshold)
                if args.cpu_threshold
                else ""
            )
            file.write(
                "Threshold: Memory Usage > {}%\n".format(args.mem_threshold)
                if args.mem_threshold
                else ""
            )
            file.write("\n")
            file.write("Timestamp, CPU Usage, Memory Usage\n")
            file.write("\n")

if args.verbose:
    print("======= CPU =======")
    print()
    print("======= Memory =======")
    print()
    print("======= Disk =======")
    print()
    print("======= Network =======")

    while True:
        cpu_percent = psutil.cpu_percent()
        cpu_freq = psutil.cpu_freq()
        cpu_max = cpu_freq.max / 1000 if cpu_freq else 0
        cpu_min = cpu_freq.min / 1000 if cpu_freq else 0

        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        mem_total = mem.total / (1024**3)
        mem_avail = mem.available / (1024**3)

        disk = psutil.disk_usage("/")
        disk_percent = disk.percent
        disk_total = disk.total / (1024**3)
        disk_avail = disk.free / (1024**3)

        network = psutil.net_io_counters()
        bytes_sent = network.bytes_sent
        bytes_recv = network.bytes_recv
        packets_sent = network.packets_sent
        packets_recv = network.packets_recv

        # Log to File
        if (args.cpu_threshold and cpu_percent > args.cpu_threshold) or (
            args.mem_threshold and mem_percent > args.mem_threshold
        ):
            with open("log.txt", "a") as file:
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                file.write(
                    f"{formatted_time}, {cpu_percent}%, {mem_percent}%, {packets_sent/1000:.2f}, {packets_recv/1000:.2f}\n"
                )

        # Move up 6 lines to CPU data
        print(
            "\033[6F",
            end="",
        )
        print(
            "\r\033[2K",
            end="",
        )
        print(
            f"CPU Usage: {cpu_percent}%  |  Max Clock: {cpu_max:.1f} GHz  |  Min Clock: {cpu_min:.1f} GHz",
            end="",
        )

        # Move down 2 lines to RAM data
        print(
            "\033[2E",
            end="",
        )
        print(
            "\r\033[2K",
            end="",
        )
        print(
            f"RAM Usage: {mem_percent}%  |  Total: {mem_total:.2f} GB  |  Available: {mem_avail:.2f} GB",
            end="",
        )

        # Move down 2 lines to Disk data
        print(
            "\033[2E",
            end="",
        )
        print(
            "\r\033[2K",
            end="",
        )
        print(
            f"Free Percent: {disk_percent}%  |  Total: {disk_total:.2f} GB  |  Available: {disk_avail:.2f} GB",
            end="",
        )

        # Move down 2 lines to Sensor Data
        print("\033[2E", end="")
        print(
            "\r\033[2K",
            end="",
        )
        print(
            f"Packets Sent: {packets_sent}  |  Packets Received: {packets_recv}  |  Bytes Sent: {bytes_sent}  | Bytes Received: {bytes_recv}",
            end="",
            flush=True,
        )

        time.sleep(interval)

else:
    print("Verbose mode is off. Use -v for more details.")

    print("======= CPU =======")
    print()
    print("======= Memory =======")
    print()
    print("======= Disk =======")

    while True:
        cpu_percent = psutil.cpu_percent()
        cpu_freq = psutil.cpu_freq()
        cpu_max = cpu_freq.max / 1000 if cpu_freq else 0
        cpu_min = cpu_freq.min / 1000 if cpu_freq else 0

        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        mem_total = mem.total / (1024**3)
        mem_avail = mem.available / (1024**3)

        disk = psutil.disk_usage("/")
        disk_percent = disk.percent
        disk_total = disk.total / (1024**3)
        disk_avail = disk.free / (1024**3)

        # Log to File
        if (args.cpu_threshold and cpu_percent > args.cpu_threshold) or (
            args.mem_threshold and mem_percent > args.mem_threshold
        ):
            with open("log.txt", "a") as file:
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                file.write(f"{formatted_time}, {cpu_percent}%, {mem_percent}%\n")

        # Move up 4 lines to CPU data
        print(
            "\033[4F",
            end="",
        )
        print(
            "\r\033[2K",
            end="",
        )
        print(
            f"CPU Usage: {cpu_percent}%  |  Max Clock: {cpu_max:.1f} GHz  |  Min Clock: {cpu_min:.1f} GHz",
            end="",
        )

        # Move down 2 lines to RAM data
        print(
            "\033[2E",
            end="",
        )
        print(
            "\r\033[2K",
            end="",
        )
        print(
            f"RAM Usage: {mem_percent}%  |  Total: {mem_total:.2f} GB  |  Available: {mem_avail:.2f} GB",
            end="",
        )

        # Move down 2 lines to Disk data
        print(
            "\033[2E",
            end="",
        )
        print(
            "\r\033[2K",
            end="",
        )
        print(
            f"Free Percent: {disk_percent}%  |  Total: {disk_total:.2f} GB  |  Available: {disk_avail:.2f} GB",
            end="",
            flush=True,
        )

        time.sleep(interval)
