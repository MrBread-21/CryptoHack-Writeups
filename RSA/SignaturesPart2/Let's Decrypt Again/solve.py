from pwn import remote
import json, random
from sympy import isprime, primerange, discrete_log
from sympy.ntheory.modular import crt
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15  # pip install pkcs1

r = remote("socket.cryptohack.org", 13394)
r.recvline()

def send(d):
    r.sendline(json.dumps(d).encode())
    return json.loads(r.recvline())

sig = int(send({"option": "get_signature"})["signature"], 16)

# 1. Our own modulus n = p^2 with p - 1 smooth -> discrete logs mod n are easy,
#    and sig must be a generator mod p^2
small = list(primerange(3, 2 ** 16))
while True:
    fs = [2] + random.sample(small, 30)
    p = 1
    for f in fs:
        p *= f
    p += 1
    if p.bit_length() > 400 and isprime(p) and all(pow(sig, (p - 1) // f, p) != 1 for f in set(fs)) \
            and pow(sig, p - 1, p * p) != 1:
        break
n = p * p
suffix = send({"option": "set_pubkey", "pubkey": hex(n)})["suffix"]

# 2. log_sig(x) mod p^2 = (log mod p-1 via Pohlig-Hellman) + (log mod p via the p-adic log)
L = lambda x: (pow(x, p - 1, n) - 1) // p
def dlog(x):
    a = discrete_log(p, x % p, sig % p)
    b = L(x) * pow(L(sig), -1, p) % p
    return int(crt([p - 1, p], [a, b])[0])

msgs = ["This is a test for a fake signature.",
        "My name is Mallory and I own CryptoHack.org",
        "Please send all my money to 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"]
shares = []
for i, m in enumerate(msgs):
    m += suffix
    e = dlog(bytes_to_long(emsa_pkcs1_v15.encode(m.encode(), 96)))
    shares.append(bytes.fromhex(send({"option": "claim", "msg": m, "e": hex(e), "index": i})["secret"]))

# 3. The flag is the XOR of the three shares
print(bytes(a ^ b ^ c for a, b, c in zip(*shares)))
#crypto{let's_decrypt_w4s_t0o_ez_do_1t_ag41n}
