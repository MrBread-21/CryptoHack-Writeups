from pwn import remote
import json
from Crypto.Util.number import long_to_bytes

r = remote("socket.cryptohack.org", 13374)
r.recvline()

def send(d):
    r.sendline(json.dumps(d).encode())
    return json.loads(r.recvline())

# "signing" is decryption: sign(c) = c^d = m
secret = send({"option": "get_secret"})["secret"]
print(long_to_bytes(int(send({"option": "sign", "msg": secret})["signature"], 16)))
#crypto{d0n7_516n_ju57_4ny7h1n6}
