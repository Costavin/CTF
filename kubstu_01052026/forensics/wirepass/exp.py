import io
import struct
import pyzipper

from scapy.all import rdpcap, TCP, Raw


#pass_dec = "48 63 79 46 6c 31 70 70 33 72 24 32 30 32 36"
password = b"IcyFl1pp3r$2026"

packets = rdpcap("challenge.pcap")
segments = []
for pkt in packets:
    if pkt.haslayer(TCP) and pkt.haslayer(Raw) and pkt[TCP].dport == 31337:
        segments.append((pkt[TCP].seq, bytes(pkt[Raw].load)))

segments.sort(key=lambda x:x[0])

done = set()
stream = b""
for seq, data in segments:
    if seq not in done:
        done.add(seq)
        stream += data

magic = stream[:4]
xor_key = stream[4:4+16]
size = struct.unpack(">I",stream[20:20+4])
encrypted = stream[24:24+size[0]]


plaintext = bytes([a ^ xor_key[i%16] for i, a in enumerate(encrypted)])

#wrap bytes in a file-like object
zip_buffer = io.BytesIO(plaintext)


with pyzipper.AESZipFile(zip_buffer,'r') as zip_ref:
    try:
        print(zip_ref.namelist())
        zip_ref.setpassword(pwd=password)
        print("Extraction successful!")
        for file in zip_ref.namelist():
            print(zip_ref.read(file).decode("utf-8"))
    except RuntimeError as e:
        print(f"Error: {e}")





