import psutil
import pandas as pd
import time
import os

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "network_data.csv")

data = []

print("Collecting network data... Press Ctrl+C to stop")

try:
    while True:
        net = psutil.net_io_counters()
        data.append({
            "timestamp": time.strftime("%H:%M:%S"),
            "bytes_sent": net.bytes_sent,
            "bytes_recv": net.bytes_recv,
            "packets_sent": net.packets_sent,
            "packets_recv": net.packets_recv
        })
        time.sleep(1)

except KeyboardInterrupt:
    df = pd.DataFrame(data)

    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    df.to_csv(CSV_PATH, index=False)
    print(f"Data saved to {CSV_PATH}")