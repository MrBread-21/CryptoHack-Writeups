from pwn import remote
import json
from Crypto.Util.number import long_to_bytes

r = remote("socket.cryptohack.org", 13386)
r.recvline()

def get_flag():
    r.sendline(json.dumps({"option": "get_flag"}).encode())
    d = json.loads(r.recvline())
    return d["encrypted_flag"], d["modulus"], d["padding"]

c1, N, (a1, b1) = get_flag()
c2, _, (a2, b2) = get_flag()
e = 11

# Franklin-Reiter: m is a common root of f1 = (a1*x + b1)^e - c1 and f2 = (a2*x + b2)^e - c2,
# so gcd(f1, f2) = x - m.  Polynomials are lists of coefficients (lowest degree first) mod N.
def mul(f, g):
    h = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            h[i + j] = (h[i + j] + x * y) % N
    return h

def poly(a, b, c):
    f = [1]
    for _ in range(e):
        f = mul(f, [b, a])
    f[0] = (f[0] - c) % N
    return f

def mod(f, g):
    f = f[:]
    while len(f) >= len(g):
        k = f[-1] * pow(g[-1], -1, N) % N
        for i in range(len(g)):
            f[len(f) - len(g) + i] = (f[len(f) - len(g) + i] - k * g[i]) % N
        f.pop()
    while f and f[-1] == 0:
        f.pop()
    return f

def gcd(f, g):
    while g:
        f, g = g, mod(f, g)
    return f

g = gcd(poly(a1, b1, c1), poly(a2, b2, c2))   # = k*(x - m)
m = -g[0] * pow(g[1], -1, N) % N
print(long_to_bytes(m))
#crypto{linear_padding_isnt_padding}
