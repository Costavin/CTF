import re

pattern = re.compile(r"[a-zA-Z0-9()_]")
res=""
with open("Weird_Furry_text.txt", "r") as file:
    for line in file:
        for match in pattern.finditer(line):
            #print(f"Match found: {match.group()}, Position: {match.span()}")
            res += match.group()
print(res)
