from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e = 3, c

# m = FLAG * 256^k  (k null bytes, FLAG is 43 bytes -> k = 57)
# => FLAG^3 = c / 256^(3k) (mod n), and FLAG^3 is only slightly bigger than n
k = 100 - 43
f3 = c * pow(256 ** (3 * k), -1, n) % n
t = 0
while not iroot(f3 + t * n, 3)[1]:
    t += 1
print(long_to_bytes(int(iroot(f3 + t * n, 3)[0])))
#crypto{n0n_574nd4rd_p4d_c0n51d3r3d_h4rmful}
