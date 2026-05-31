import io
import struct
import pyzipper

from scapy.all import rdpcap, TCP, Raw


packets = rdpcap("Ratte.pcap")
segments = []
for i,pkt in enumerate(packets,1):
    if pkt.haslayer(TCP) and pkt[TCP].dport == 1337:
        segments.append((i, bytes(pkt[TCP].payload)))    #No., tcp_data

segments.sort(key=lambda x:x[0])
print(segments)

done = set()
stream = b""
for seq, data in segments:
    if seq not in done:
        done.add(seq)
        stream += data

print(" ".join(f'{b:02x}' for b in stream))

magic = stream[:4]
xor_key = stream[4:4+1]                     #lets try with one key byte,then lets see if better to window it or choose another combination
#size = struct.unpack(">I",stream[20:20+4])
encrypted = stream[5:]
print(magic, xor_key, encrypted, len(encrypted))

#0t,1t,2@,3f,4f,5t,6t,7@,8f,9f 
plaintext = bytes([a ^ int.from_bytes(xor_key) for a in encrypted])
print(plaintext)
offset = 0
flag = b""
for b in plaintext:
    flag += plaintext[offset+3:offset+3+2]
    offset+=5
#wrap bytes in a file-like object
print(flag)

