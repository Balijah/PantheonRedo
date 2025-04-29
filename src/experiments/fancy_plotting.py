import os
import matplotlib.pyplot as plt

# Set the correct data directory!
DATA_DIR = "data"

# CC schemes you tested
schemes = ["cubic", "scream", "fillp"]

# Make a folder for plots if it doesn't exist
os.makedirs("plots", exist_ok=True)

for scheme in schemes:
    data_file = os.path.join(DATA_DIR, f"{scheme}_datalink_run1.log")
    if not os.path.exists(data_file):
        print(f"[!] Data file for {scheme} not found at {data_file}")
        continue

    # Parse the throughput over time
    throughputs = []
    times = []

    with open(data_file, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "#" in line:
                timestamp, packet_size = line.split("#")
                timestamp = float(timestamp.strip())
                packet_size = float(packet_size.strip())
                throughputs.append(packet_size * 8 / 1000)  # kbps
                times.append(timestamp / 1000)  # convert ms to seconds

    if not throughputs:
        print(f"[!] No valid throughput data for {scheme}, skipping plot.")
        continue

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(times, throughputs, label=f"{scheme} throughput (kbps)")
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (kbps)")
    plt.title(f"Throughput vs Time - {scheme}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/{scheme}_throughput.png")
    plt.close()

print("✅ Done! Check the 'plots/' directory for your graphs.")

