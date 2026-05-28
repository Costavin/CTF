import io
import struct
import pyzipper
import base64
from scapy.all import rdpcap, DNS, UDP


encoded_data = "SGVsbG8gV29ybGQh"

# 1. Decode Base64 to bytes
decoded_bytes = base64.b64decode(encoded_data)

# 2. Convert bytes back to a readable string (UTF-8)
decoded_string = decoded_bytes.decode('utf-8')




packets = rdpcap("Krasnodar.pcap")
segments = []
for i,pkt in enumerate(packets,1):
    if pkt.haslayer(DNS) and pkt[UDP].dport == 53:
        segments.append((i, pkt[DNS].qd.qname))  

segments.sort(key=lambda x:x[0])
print(segments)

done = set()
extracted = []

for seq, data in segments:
    if seq not in done:
        if data[0] == ord('v') and data[1:3].isdigit() and data[3] == ord('.'):
            extracted.append((data[1:3],data[4:8]))

extracted.sort(key=lambda x:x[0])
print(extracted)

flag = b"".join([a[1] for a in extracted])
print(flag)

print(bytes.fromhex(flag))


