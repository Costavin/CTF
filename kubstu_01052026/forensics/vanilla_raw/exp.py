with open("memory.raw","rb") as memory:
    chunk = 1024*1024
    offset = 0
    while True:
        data = memory.read(chunk)
        if not data:
            print("nothing")
            break

        for i,b in enumerate(data):
            if b != 0 and ord("K") == b:
                print(offset+i)
                start_pos = offset + i
                memory.seek(start_pos)   #so as not read evrything
                print(f"Chunk size: {offset}")
                payload = memory.read(64)
                #print("String found: " + " ".join(f'{b:02x}' for b in payload))
                print(f"Plain value: {payload}")
                #exit()
        offset += chunk
