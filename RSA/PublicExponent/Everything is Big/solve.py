from math import isqrt
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # N, e, c

# Wiener's attack: d is small (256 bits) -> k/d is a convergent of the continued fraction of e/N
def convergents(a, b):
    p0, p1, q0, q1 = 0, 1, 1, 0
    while b:
        t = a // b
        a, b = b, a - t * b
        p0, p1, q0, q1 = p1, t * p1 + p0, q1, t * q1 + q0
        yield p1, q1

for k, d in convergents(e, N):
    if k and (e * d - 1) % k == 0:
        phi = (e * d - 1) // k
        s = N - phi + 1                      # p + q
        if s * s - 4 * N >= 0 and isqrt(s * s - 4 * N) ** 2 == s * s - 4 * N:
            print(long_to_bytes(pow(c, d, N)))
            break
#crypto{s0m3th1ng5_c4n_b3_t00_b1g}
