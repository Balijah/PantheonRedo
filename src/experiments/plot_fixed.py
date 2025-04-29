import os
import matplotlib.pyplot as plt

def process_log(filepath):
    times = []
    sizes = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('#') or '+' in line or '-' in line:
                continue
            time_ms, rest = line.strip().split('#')
            time_ms = float(time_ms.strip())
            size = int(rest.strip())
            times.append(time_ms / 1000.0)  # convert to seconds
            sizes.append(size)
    return times, sizes

def plot_throughput(times, sizes, scheme):
    bins = range(0, int(max(times)) + 2)
    throughput = [0] * len(bins)
    for t, s in zip(times, sizes):
        bin_idx = int(t)
        throughput[bin_idx] += s * 8  # bytes -> bits

    throughput_mbps = [b / 1e6 for b in throughput]

    plt.figure()
    plt.plot(bins, throughput_mbps, marker='o')
    plt.xlabel('Time (s)')
    plt.ylabel('Throughput (Mbps)')
    plt.title(f'Time-Series Throughput: {scheme}')
    plt.grid()
    plt.savefig(f'{scheme}_throughput.png')
    print(f"[+] Saved {scheme}_throughput.png")

schemes = ["cubic", "scream", "fillp"]

for scheme in schemes:
    filepath = f"data/{scheme}_datalink_run1.log"
    if os.path.exists(filepath):
        times, sizes = process_log(filepath)
        if times:
            plot_throughput(times, sizes, scheme)
        else:
            print(f"[!] No data for {scheme}, skipping...")
    else:
        print(f"[!] Log file not found for {scheme}")

