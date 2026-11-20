import re, json, random
from math import gcd
from pwn import remote

src = open("13398.py").read()
N, phi, g = [int(re.search(k + r" = (\d+)", src).group(1)) for k in ("N", "phi", "g")]

# 1. Factor N using phi (same trick as factoring with a known d):
#    phi = 2^s * t, a^t squared repeatedly gives non-trivial square roots of 1
def factor(N, phi):
    t = phi
    while t % 2 == 0:
        t //= 2
    factors, todo = set(), [N]
    while todo:
        n = todo.pop()
        if all(pow(a, n - 1, n) == 1 for a in (2, 3, 5, 7)):
            factors.add(n)
            continue
        while True:
            x = pow(random.randrange(2, n), t, n)
            y = pow(x, 2, n)
            while y != 1:
                x, y = y, pow(y, 2, n)
            f = gcd(x - 1, n)
            if 1 < f < n:
                todo += [f, n // f]
                break
    return factors

primes = factor(N, phi)
# 2. g is a quadratic residue mod every prime -> every power g^k is a residue too.
#    A random number is a residue mod all primes with negligible probability.
qr = [p for p in primes if pow(g, (p - 1) // 2, p) == 1]
print(len(primes), "primes,", len(qr), "where g is a QR")

def is_power_of_g(x):
    return all(pow(x, (p - 1) // 2, p) == 1 for p in qr)

r = remote("socket.cryptohack.org", 13398)
r.recvline()
def get_bit(i):
    r.sendline(json.dumps({"option": "get_bit", "i": i}).encode())
    return int(json.loads(r.recvline())["bit"], 16)

# ask each bit a few times: a random number can pass the test by luck, g^k always passes
bits = "".join("1" if all(is_power_of_g(get_bit(i)) for _ in range(4)) else "0" for i in range(43 * 8))
flag = bytes(int(bits[i:i + 8][::-1], 2) for i in range(0, len(bits), 8))  # bit i%8 is LSB-first
print(flag)
#crypto{0ver3ng1neering_ch4lleng3_s0lution$}
