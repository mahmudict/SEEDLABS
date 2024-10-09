#!/usr/bin/env python3
import os
import struct
import fcntl

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'hasan%d', IFF_TUN | IFF_NO_PI)
ifname_bytes  = fcntl.ioctl(tun, TUNSETIFF, ifr)

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

# Configure interface
os.system("ip addr add 192.168.53.99/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))

# Generate arbitrary data
arbitrary_data = input("Enter data to send to TUN interface: ").encode()

# Write arbitrary data to the TUN interface
os.write(tun, arbitrary_data)

# Report observation
print("Arbitrary data written to TUN interface:", arbitrary_data)
