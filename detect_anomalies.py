import pandas as pd
import os
from sklearn.ensemble import IsolationForest

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "network_rates.csv")
OUT_PATH = os.path.join(BASE_DIR, "data", "network_anomalies.csv")

# Load processed data
df = pd.read_csv(DATA_PATH)

# Features used for anomaly detection
features = [
    "bytes_sent_per_sec",
    "bytes_recv_per_sec",
    "packets_sent_per_sec",
    "packets_recv_per_sec"
]

# Train Isolation Forest
model = IsolationForest(
    contamination=0.05,  # 5% anomalies
    random_state=42
)

df["anomaly"] = model.fit_predict(df[features])

# Save output
df.to_csv(OUT_PATH, index=False)

print("Anomaly detection complete. Saved as network_anomalies.csv")