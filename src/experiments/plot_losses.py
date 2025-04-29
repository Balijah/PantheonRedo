# plot_losses.py
import os
import matplotlib.pyplot as plt

# Path to the data directory
data_dir = os.path.expanduser('~/Desktop/pantheon/src/experiments/data')

# List of your schemes
schemes = ['cubic', 'scream', 'fillp']

# For each scheme, parse losses and plot
for scheme in schemes:
    datalink_file = os.path.join(data_dir, f'{scheme}_datalink_run1.log')

    if not os.path.exists(datalink_file):
        print(f"[!] Log not found for {scheme}, skipping...")
        continue

    losses_per_second = {}

    with open(datalink_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            if '-' in line:
                parts = line.split('-')
                timestamp_part = parts[0].strip()
                try:
                    timestamp = float(timestamp_part)
                    second = int(timestamp // 1000)
                    losses_per_second[second] = losses_per_second.get(second, 0) + 1
                except ValueError:
                    continue

    if not losses_per_second:
        print(f"[!] No loss events found for {scheme}, skipping...")
        continue

    # Plotting
    seconds = sorted(losses_per_second.keys())
    losses = [losses_per_second[sec] for sec in seconds]

    plt.figure()
    plt.plot(seconds, losses, marker='o')
    plt.title(f'Packet Losses Over Time ({scheme})')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Number of Losses')
    plt.grid(True)
    plt.savefig(f'{scheme}_losses_timeseries.png')
    plt.close()

    print(f"[+] Saved loss time-series plot for {scheme} as {scheme}_losses_timeseries.png")

