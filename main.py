from scapy.all import sniff
from packet_capture import process_packet

print("="*60)
print("SMART NETWORK TRAFFIC ANALYZER")
print("="*60)

print("Capturing packets...\n")

sniff(
    prn=process_packet,
    store=False
)
