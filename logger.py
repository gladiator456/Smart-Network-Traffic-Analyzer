import csv
import os

FILE="logs/packets.csv"

def save_packet(src,dst,sport,dport,protocol,size):

    exists=os.path.isfile(FILE)

    with open(FILE,"a",newline="") as f:

        writer=csv.writer(f)

        if not exists:

            writer.writerow([
                "Source IP",
                "Destination IP",
                "Source Port",
                "Destination Port",
                "Protocol",
                "Packet Size"
            ])

        writer.writerow([
            src,
            dst,
            sport,
            dport,
            protocol,
            size
        ])
