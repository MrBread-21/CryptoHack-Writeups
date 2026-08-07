text = "label"

result = ""

for c in text:
    result += chr(ord(c) ^ 13)

print(f"crypto{{{result}}}")
#crypto{aloha}