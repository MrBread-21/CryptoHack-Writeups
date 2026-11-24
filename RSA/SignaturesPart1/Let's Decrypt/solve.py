from pwn import remote
import json
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15  # pip install pkcs1

r = remote("socket.cryptohack.org", 13391)
r.recvline()

def send(d):
    r.sendline(json.dumps(d).encode())
    return json.loads(r.recvline())

sig = int(send({"option": "get_signature"})["signature"], 16)
msg = "I am Mallory and I own CryptoHack.org"
digest = bytes_to_long(emsa_pkcs1_v15.encode(msg.encode(), 256))

# We choose the public key: e = 1 and n = sig - digest  ->  sig^1 mod n = digest
print(send({"option": "verify", "msg": msg, "N": hex(sig - digest), "e": "0x1"}))
#crypto{dupl1c4t3_s1gn4tur3_k3y_s3l3ct10n}
