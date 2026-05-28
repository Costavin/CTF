with open("memory.raw","rb") as memory:
    offset = 1039150061
    flag = ""
    memory.seek(offset)
    to_extract = memory.read(200)
    for i in range(0,40):
        flag += chr(to_extract[i*4])
    print(flag)

#xxd --seek 1039150061 -l 100 memory.raw

