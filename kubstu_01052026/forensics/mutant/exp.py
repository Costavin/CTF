import zlib
import base64

def get_flag(x):
    s = ""
    for el in x:
        offset = el.find("(")
        s += el[offset+1]
    return s

with open("crypt.pdf","r") as mut:
    data = mut.read()

obj5_start = data.find("5 0 obj")

stream_start = data.find('stream', obj5_start) + len("stream")
stream_end = data.find('endstream', stream_start)

stream = data[stream_start:stream_end].strip()
print(stream[2:-2])



# For ASCII85 decoding (the <~ part)
decoded_ascii85 = base64.a85decode(stream[2:-2])
# Then decompress the FlateDecode data
original_data = zlib.decompress(decoded_ascii85).decode('utf-8')
for x in original_data.split("\n"):
    print(x)

print(get_flag(original_data.split("\n")))
