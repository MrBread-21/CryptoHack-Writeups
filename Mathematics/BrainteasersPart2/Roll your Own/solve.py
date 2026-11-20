from pwn import remote
import json

r = remote("socket.cryptohack.org", 13403)
q = int(r.recvline().split(b": ")[1].strip().strip(b'"'), 16)

# n = q^2, g = 1 + q  ->  g^x = 1 + x*q (mod q^2)  (binomial theorem), and g^q = 1
r.sendline(json.dumps({"g": hex(1 + q), "n": hex(q * q)}).encode())
h = int(r.recvline().split(b": ")[-1].strip().strip(b'"'), 16)
r.sendline(json.dumps({"x": hex((h - 1) // q)}).encode())
print(r.recvline())
#crypto{Grabbing_Flags_with_Pascal_Paillier}
