from pwn import *
import json

r = remote("socket.cryptohack.org", 11112)

for _ in range(4):
    print(r.recvline().decode(), end="")

r.sendline(json.dumps({"buy": "flag"}).encode())

print(json.loads(r.recvline().decode()))

r.close()