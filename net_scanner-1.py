import scapy.all as scapy

arp_request_packet = scapy.ARP(pdst = "192.168.1.0/16")

broadcast_packet = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

combined_packet = arp_request_packet/broadcast_packet

result = scapy.srp(combined_packet, timeout = 1)

print(result)

