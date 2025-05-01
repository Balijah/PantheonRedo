Great! Based on your progress and the assignment requirements from the PDF, here's a **simple and complete `README.md`** tailored to your project:

---

```markdown
# Pantheon Congestion Control Evaluation

## Overview

This project is part of Programming Assignment 3 for Computer Networks. The goal was to evaluate different congestion control (CC) schemes using Pantheon and Mahimahi under two emulated network conditions.

## Environment Setup

1. **Platform**: Ubuntu 20.04 (running on VirtualBox)
2. **Pantheon repo**: [https://github.com/StanfordSNR/pantheon](https://github.com/StanfordSNR/pantheon)
3. **Dependencies**:
   - `python2`
   - `python3`
   - `mahimahi`
   - Python packages: `matplotlib`, `numpy`

## Congestion Control Schemes Tested

- `cubic`
- `scream`
- `fillp`

## Network Profiles Emulated

1. **Low-Latency, High-Bandwidth**:  
   - Bandwidth: 50 Mbps  
   - RTT: 10 ms

2. **High-Latency, Constrained-Bandwidth**:  
   - Bandwidth: 1 Mbps  
   - RTT: 200 ms

## Experiment Methodology

Each experiment was run using:
```bash
python2 test.py local --schemes "cubic scream fillp" --uplink-trace tests/<trace>.trace --downlink-trace tests/<trace>.trace --runtime 60
```

All log files were saved under `src/experiments/data`.

The `analyze.py` script from Pantheon was used to generate:
- Throughput over time plots
- Delay (RTT) plots

Additional custom scripts were created to:
- Plot **loss rate** over time
- Compute and visualize **average and 95th-percentile RTT**
- Generate a **summary scatter plot** (RTT vs. Throughput)

## How to Reproduce

1. Clone this repo and navigate into it:
```bash
git clone <your-repo-url>
cd pantheon
```

2. Install required packages:
```bash
sudo apt update
sudo apt install python2 python3 mahimahi python3-pip
pip3 install matplotlib numpy
```

3. Run the experiments:
```bash
cd src/experiments
python2 test.py local --schemes "cubic scream fillp" --uplink-trace tests/50mbps_10ms_data.trace --downlink-trace tests/50mbps_10ms_ack.trace --runtime 60
```

4. Generate analysis graphs:
```bash
cd ../../analysis
python3 analyze.py --data-dir ../experiments/data
```

5. Run custom plotting:
```bash
cd ../experiments
python3 fancy_plotting.py
python3 loss_plotting.py
python3 rtt_vs_throughput_summary.py
```

## Directory Structure

```
pantheon/
├── src/
│   ├── analysis/              # analyze.py, plot.py, report.py
│   ├── experiments/           # test.py, custom plotting scripts, trace files
│   │   ├── data/              # generated logs and graphs
│   │   ├── tests/             # 1mbps_200ms and 50mbps_10ms trace files
├── README.md
```

## Scripts

- `fancy_plotting.py`: Individual throughput graphs per scheme.
- `loss_plotting.py`: Time-series loss visualization.
- `rtt_vs_throughput_summary.py`: Summary scatter plot for RTT vs. throughput.

## Notes

- Only `cubic`, `scream`, and `fillp` were tested successfully.
- Other schemes such as `vivace` and `taova` encountered runtime errors and were excluded.
- Trace files were manually created with realistic values to emulate network conditions.

## Lessons Learned

> _To be filled in your PDF report (Part 7 of the assignment)._

## Author

Burhan Khan – Spring 2025 – CS Networks
```

---

Let me know if you’d like to add usage screenshots, command output samples, or links to any reports.
