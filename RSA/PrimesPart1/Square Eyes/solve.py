from math import isqrt
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, ct
p = isqrt(n)  # n = p^2  ->  phi(n) = p * (p - 1)
d = pow(e, -1, p * (p - 1))
print(long_to_bytes(pow(ct, d, n)))
#crypto{squar3_r00t_i5_f4st3r_th4n_f4ct0r1ng!}
