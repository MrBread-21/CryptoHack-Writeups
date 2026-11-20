from itertools import combinations
from gmpy2 import iroot
from sympy.ntheory.modular import crt
from Crypto.Util.number import long_to_bytes

blocks = open("output.txt").read().split("\n\n")
keys = []
for b in blocks:
    if b.strip():
        v = dict(l.split(" = ") for l in b.strip().splitlines())
        keys.append((int(v["n"]), int(v["c"])))

# Hastad broadcast (e = 3): if the same m is sent to 3 people, CRT gives m^3 exactly.
# Not every message is the same -> try every group of 3.
for group in combinations(keys, 3):
    m3 = int(crt([n for n, _ in group], [c for _, c in group])[0])
    m, exact = iroot(m3, 3)
    if exact:
        print(long_to_bytes(int(m)))
        break
#crypto{1f_y0u_d0nt_p4d_y0u_4r3_Vuln3rabl3}
