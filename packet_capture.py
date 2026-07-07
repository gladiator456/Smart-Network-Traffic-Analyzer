from scapy.layers.inet import IP,TCP,UDP,ICMP
from logger import save_packet
from packet_statistics import update_statistics

def process_packet(packet):

    if not packet.haslayer(IP):
        return

    ip = packet[IP]

    protocol="OTHER"

    src_port="-"
    dst_port="-"

    if packet.haslayer(TCP):
        protocol="TCP"
        src_port=packet[TCP].sport
        dst_port=packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol="UDP"
        src_port=packet[UDP].sport
        dst_port=packet[UDP].dport

    elif packet.haslayer(ICMP):
        protocol="ICMP"

    src_ip=ip.src
    dst_ip=ip.dst

    packet_size=len(packet)

    print("-----------------------------------------------")
    print(f"Protocol : {protocol}")
    print(f"Source IP : {src_ip}:{src_port}")
    print(f"Destination IP : {dst_ip}:{dst_port}")
    print(f"Packet Size : {packet_size}")

    save_packet(
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        packet_size
    )

    update_statistics(protocol)
