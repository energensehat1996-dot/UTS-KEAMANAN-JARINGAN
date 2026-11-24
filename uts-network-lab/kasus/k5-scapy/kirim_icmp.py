import sys
from scapy.all import IP, ICMP, send

target = sys.argv[1]
paket = IP(dst=target)/ICMP()
send(paket)
