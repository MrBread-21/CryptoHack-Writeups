from sympy import factorint
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, ct
p, q = factorint(n)  # n is only ~200 bits -> easy to factor
d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(ct, d, n)))
#crypto{N33d_b1g_pR1m35}
