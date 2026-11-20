from gmpy2 import isqrt, is_square
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, c

# p and q are very close -> Fermat factorization: n = a^2 - b^2
a = isqrt(n) + 1
while not is_square(a * a - n):
    a += 1
b = isqrt(a * a - n)
p, q = a + b, a - b
print(long_to_bytes(pow(c, pow(e, -1, (p - 1) * (q - 1)), n)))
#crypto{f3rm47_w45_4_g3n1u5}
