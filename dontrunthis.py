import multiprocessing
import time
import math
import os

def cpu_task(duration_seconds):
    end_time = time.time() + duration_seconds
    x = 0.0

    while time.time() < end_time:
        # CPU-heavy calculation
        x += math.sqrt(12345.6789) * math.sin(x)

    return x

if __name__ == "__main__":
    duration = 30  # seconds
    cores = os.cpu_count()

    print(f"Using {cores} CPU cores for {duration} seconds...")

    with multiprocessing.Pool(processes=cores) as pool:
        pool.map(cpu_task, [duration] * cores)

    print("Done.")