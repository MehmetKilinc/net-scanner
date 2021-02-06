import scapy.all as scapy

arp_request_packet = scapy.ARP()
scapy.ls(scapy.ARP())
broadcast_packet = scapy.Ether()
scapy.ls(scapy.Ether())