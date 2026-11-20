from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e = 3, ct
# m^3 < n -> no modular reduction happened, just take the integer cube root
print(long_to_bytes(int(iroot(ct, 3)[0])))
#crypto{N33d_m04R_p4dd1ng}
