import json
from hashlib import sha256
from math import gcd
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

lines = open("output.txt").read().splitlines()
N, a, b = [int(l.split("= ")[1]) for l in lines[:3]]
data = json.loads(lines[3])

# gcd(N^a - 1, N^b - 1) = N^gcd(a, b) - 1
g = N ** gcd(a, b) - 1
key = sha256(long_to_bytes(g)).digest()[:16]
print(AES.new(key, AES.MODE_CBC, bytes.fromhex(data["iv"])).decrypt(bytes.fromhex(data["ct"])))
#crypto{n0_r34$0n_t0_b05h3r_w1th_l4rG3_GCD}
