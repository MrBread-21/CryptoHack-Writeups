from pwn import remote
import json, sys, random
from sympy import isprime, primerange
from sympy.ntheory import discrete_log
sys.path.append("../../Starter/Deriving Symmetric Keys")
from decrypt import decrypt_flag

r = remote("socket.cryptohack.org", 13378)
recv = lambda: json.loads(r.recvuntil(b"}").split(b": ", 1)[1])
alice, bob, msg = recv(), recv(), recv()
p, A = int(alice["p"], 16), int(alice["A"], 16)

# Bob insists on g = 2 and a prime p, but accepts OUR prime.
# Use a bigger prime p2 with p2 - 1 smooth -> Pohlig-Hellman recovers Bob's static secret b.
small = list(primerange(3, 2 ** 16))
while True:
    p2 = 2
    while p2 < p:
        p2 *= random.choice(small)
    p2 += 1
    if isprime(p2):
        break

r.sendlineafter(b"parameters: ", json.dumps({"p": hex(p2), "g": "0x02", "A": "0x1234567"}).encode())
B2 = int(recv()["B"], 16)
b = discrete_log(p2, B2, 2)
print(decrypt_flag(pow(A, b, p), msg["iv"], msg["encrypted"]))
#crypto{uns4f3_pr1m3_sm4ll_oRd3r}
