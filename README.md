# Smart Network Traffic Analyzer

A lightweight network traffic analyzer built using Python and Scapy. The project captures live packets from the network interface, extracts protocol-level information, logs packet metadata, and provides basic traffic statistics.

## Features

- Live packet capture
- IPv4 packet parsing
- TCP / UDP / ICMP detection
- Source & Destination IP extraction
- Source & Destination Port extraction
- Packet size analysis
- CSV packet logging
- Protocol-wise statistics

## Technologies

- Python
- Scapy
- Pandas
- Matplotlib

## Project Structure

```
Smart-Network-Traffic-Analyzer
│
├── main.py
├── packet_capture.py
├── packet_statistics.py
├── logger.py
├── requirements.txt
├── logs/
│   └── packets.csv
├── screenshots/
└── README.md
```

## Current Status

✔ Live packet capture implemented

✔ Protocol analysis implemented

✔ CSV logging implemented

✔ Traffic statistics implemented

## Planned Features

- Real-time dashboard
- Suspicious IP detection
- SYN Flood Detection
- Port Scan Detection
- Traffic Visualization
- AI-based anomaly detection

## Installation

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

## Author

Anuj Saxena
