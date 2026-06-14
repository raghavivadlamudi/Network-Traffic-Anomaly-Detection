import pandas as pd
import os

# Paths (safe & professional)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "network_data.csv")
OUT_PATH = os.path.join(BASE_DIR, "data", "network_rates.csv")

# Load raw data
df = pd.read_csv(DATA_PATH)

# Convert cumulative counters → per-second rates
df["bytes_sent_per_sec"] = df["bytes_sent"].diff()
df["bytes_recv_per_sec"] = df["bytes_recv"].diff()
df["packets_sent_per_sec"] = df["packets_sent"].diff()
df["packets_recv_per_sec"] = df["packets_recv"].diff()

# Remove first row (NaN after diff)
df = df.dropna()

# Save processed data
df.to_csv(OUT_PATH, index=False)

print("Processed data saved as network_rates.csv")