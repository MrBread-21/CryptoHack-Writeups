import json, random
from pwn import remote
from sympy import isprime, jacobi_symbol, primerange
from sympy.ntheory.modular import crt

# Arnault's method: n = p1*p2*p3, p_i = k_i*(p1 - 1) + 1, chosen so that
# (a / p_i) = -1 for every base a < 64  ->  n passes Miller-Rabin for all those bases
bases = list(primerange(2, 64))
k = [1, 67, 127]  # found by a small search (see writeup)

def legendre_ok(a, x):  # p1 = x (mod 4a) makes (a / p_i) = -1 for all three p_i
    return all(jacobi_symbol(a, (ki * (x - 1) + 1) % (4 * a)) == -1 for ki in k)

def residues(c):  # allowed p1 mod each base, given p1 = c (mod 8)
    res = {8: [c] if legendre_ok(2, c) else []}
    for a in bases[1:]:
        res[a] = [x % a for x in range(c % 4, 4 * a, 4) if (k[1] * (x - 1) + 1) % a and (k[2] * (x - 1) + 1) % a and legendre_ok(a, x)]
    return res

allowed = next(r for r in map(residues, range(1, 8, 2)) if all(r.values()))
# extra conditions so that n = 1 (mod k_i):  p1 * p3 = 1 (mod k2),  p1 * p2 = 1 (mod k3)
allowed[k[1]] = [y for y in range(k[1]) if y * (k[2] * (y - 1) + 1) % k[1] == 1]
allowed[k[2]] = [y for y in range(k[2]) if y * (k[1] * (y - 1) + 1) % k[2] == 1]

def miller_rabin(n):  # copy of the server's check
    r, s = 0, n - 1
    while s % 2 == 0:
        r, s = r + 1, s // 2
    for b in bases:
        x = pow(b, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

mods = list(allowed)
while True:
    x0, M = crt(mods, [random.choice(allowed[m]) for m in mods])
    p1 = int(x0) + int(M) * random.getrandbits(150)
    p2, p3 = k[1] * (p1 - 1) + 1, k[2] * (p1 - 1) + 1
    if isprime(p1) and isprime(p2) and isprime(p3) and miller_rabin(p1 * p2 * p3):
        break
n = p1 * p2 * p3
print("n bits:", n.bit_length())

# base = p1  ->  p1^(n-1) mod n is a multiple of p1, i.e. huge -> FLAG[:x] is the whole flag
r = remote("socket.cryptohack.org", 13385)
r.recvline()
r.sendline(json.dumps({"prime": n, "base": p1}).encode())
print(r.recvline())
#crypto{Forging_Primes_with_Francois_Arnault}
