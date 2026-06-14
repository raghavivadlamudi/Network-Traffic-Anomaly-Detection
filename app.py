import pandas as pd
import streamlit as st
import os

st.set_page_config(page_title="Network Anomaly Dashboard", layout="wide")

st.title("🚨 Network Anomaly Detection Dashboard")

# Get absolute project path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "network_anomalies.csv")

# Load data
df = pd.read_csv(DATA_PATH)

# Separate normal and anomalous data
normal = df[df["anomaly"] == 1]
anomaly = df[df["anomaly"] == -1]

st.subheader("📈 Network Traffic (Bytes Received per Second)")
st.line_chart(
    normal.set_index("timestamp")["bytes_recv_per_sec"]
)

st.subheader("🔴 Detected Anomalies")
st.scatter_chart(
    anomaly.set_index("timestamp")["bytes_recv_per_sec"]
)

st.markdown("""
### 🔍 Explanation
- **Blue line** → normal network behavior  
- **Red dots** → anomalous spikes detected using Isolation Forest  
""")