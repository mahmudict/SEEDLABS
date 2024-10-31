#!/usr/bin/env python3
from scapy.all import *
ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=48701, dport=23, flags="A", seq=3615143569)
pkt = ip/tcp
ls(pkt)
send(pkt,iface="br-d9df92208b54", verbose=0)
