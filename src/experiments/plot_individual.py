import matplotlib.pyplot as plt
import os

schemes = ["cubic", "scream", "fillp"]
data_dir = "./data"  # Assuming you are in ~/Desktop/pantheon/src/experiments/

for scheme in schemes:
    throughput = []
    timestamps = []

    datalink_log_path = os.path.join(data_dir, f"{scheme}_datalink_run1.log")
    if not os.path.exists(datalink_log_path):
        print(f"No log file for {scheme}, skipping.")
        continue

    with open(datalink_log_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "#" not in line:
                continue  # Skip lines without #
            
            time_part, size_part = line.split("#")
            timestamp_ms = float(time_part.strip())
            size_bytes = int(size_part.strip())
            
            throughput.append(size_bytes * 8 / 1000.0)  # kilobits
            timestamps.append(timestamp_ms / 1000.0)    # convert ms to seconds

    if len(timestamps) == 0:
        print(f"No usable throughput data for {scheme}, skipping.")
        continue

    # Plot
    plt.figure()
    plt.plot(timestamps, throughput, marker='o', label=f"{scheme} throughput")
    plt.xlabel('Time (s)')
    plt.ylabel('Throughput (kbps)')
    plt.title(f"Throughput Over Time: {scheme}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{scheme}_throughput.png")
    plt.close()

print("Done plotting!")

