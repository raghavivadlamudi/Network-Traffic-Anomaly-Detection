# Network Traffic Anomaly Detection System

## Overview

A real-time Network Traffic Anomaly Detection System developed using Python, Streamlit, and Machine Learning. The project monitors network traffic metrics, processes network data, and identifies anomalous traffic patterns using the Isolation Forest algorithm.

## Features

* Real-time network traffic monitoring
* Collection of bandwidth and packet statistics
* Traffic rate calculation and preprocessing
* Anomaly detection using Isolation Forest
* Interactive Streamlit dashboard for visualization
* Network traffic trend analysis

## Project Structure

```text
Network-Traffic-Anomaly-Detection/
│
├── collector/
├── dashboard_app/
├── data/
├── model/
├── README.md
├── requirements.txt
└── .gitignore
```

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* psutil

## Workflow

1. Collect network traffic metrics.
2. Process and clean collected data.
3. Calculate traffic rates and statistics.
4. Detect anomalies using Isolation Forest.
5. Visualize results through a Streamlit dashboard.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Enhancements

* Real-time alert notifications
* Cloud deployment
* Advanced anomaly detection models
* Historical traffic trend analysis

## Author

Raghavi Vadlamudi
