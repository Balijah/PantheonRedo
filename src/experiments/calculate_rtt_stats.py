# calculate_rtt_stats.py
import os
import numpy as np

# Path to the data directory
data_dir = os.path.expanduser('~/Desktop/pantheon/src/experiments/data')

# List of your schemes
schemes = ['cubic', 'scream', 'fillp']

# RTT results
rtt_stats = {}

for scheme in schemes:
    uplink_log = os.path.join(data_dir, f'{scheme}_mm_datalink_run1.log')

    if not os.path.exists(uplink_log):
        print(f"[!] Uplink log not found for {scheme}, skipping...")
        continue

    delays = []

    with open(uplink_log, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            if '-' in line:
                parts = line.split('-')
                try:
                    # Format: timestamp - packet size delay_ms flow
                    timestamp = float(parts[0].strip())
                    rest = parts[1].strip().split()
                    delay_ms = float(rest[1])
                    delays.append(delay_ms)
                except (IndexError, ValueError):
                    continue

    if delays:
        avg_rtt = np.mean(delays)
        p95_rtt = np.percentile(delays, 95)
        rtt_stats[scheme] = (avg_rtt, p95_rtt)
    else:
        print(f"[!] No RTT data for {scheme}, skipping...")

# Print nicely
print("\n=== RTT Statistics ===")
for scheme, (avg_rtt, p95_rtt) in rtt_stats.items():
    print(f"{scheme.capitalize()}: Average RTT = {avg_rtt:.2f} ms, 95th Percentile RTT = {p95_rtt:.2f} ms")

