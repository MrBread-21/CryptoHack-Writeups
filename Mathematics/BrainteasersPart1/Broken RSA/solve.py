from sympy.ntheory import sqrt_mod
from Crypto.Util.number import long_to_bytes

exec(open("broken_rsa.txt").read())  # n (a prime!), e = 16, ct

# e = 16 = 2^4 -> take the modular square root 4 times, keeping every branch
roots = [ct]
for _ in range(4):
    roots = [r for x in roots for r in (sqrt_mod(x, n, all_roots=True) or [])]

for m in roots:
    if b"crypto" in long_to_bytes(m):
        print(long_to_bytes(m))
#crypto{m0dul4r_squ4r3_r00t}
