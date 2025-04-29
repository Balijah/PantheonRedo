import matplotlib.pyplot as plt
import os
from collections import defaultdict

# Paths to your two experiments
data_dirs = {
    "run1": "/home/vboxuser/Desktop/pantheon/src/experiments/data"
}

schemes = ['cubic', 'vivace', 'taova']

def parse_simple_log(filepath):
    timestamps = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('#')
            if len(parts) < 2:
                continue
            ts = float(parts[0].strip())
            timestamps.append(ts)
    return timestamps

def calculate_throughput(timestamps):
    if not timestamps:
        return [], []
    
    # Normalize timestamps to start from 0
    first_ts = timestamps[0]
    normalized_ts = [ts - first_ts for ts in timestamps]
    
    # Bin into seconds
    counter = defaultdict(int)
    for ts in normalized_ts:
        second = int(ts)
        counter[second] += 1

    seconds_sorted = sorted(counter.keys())
    throughputs = []
    times = []
    for sec in seconds_sorted:
        pkts = counter[sec]
        throughput_mbps = (pkts * 1500 * 8) / 1e6  # bytes to megabits
        throughputs.append(throughput_mbps)
        times.append(sec)

    return times, throughputs

def plot_individual(x, y, scheme, run_name):
    plt.figure(figsize=(10,6))
    plt.plot(x, y, label=scheme)
    plt.title(f"Throughput Over Time - {scheme} - {run_name}")
    plt.xlabel('Time (s)')
    plt.ylabel('Throughput (Mbps)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{scheme}_throughput_{run_name}.png")
    plt.close()

for run_name, data_dir in data_dirs.items():
    for scheme in schemes:
        log_path = os.path.join(data_dir, f"{scheme}_datalink_run1.log")
        if os.path.exists(log_path):
            timestamps = parse_simple_log(log_path)
            times, throughputs = calculate_throughput(timestamps)
            if times:
                plot_individual(times, throughputs, scheme, run_name)
        else:
            print(f"[Warning] Log not found: {log_path}")

print("✅ Individual scheme graphs generated!")

