# Null or Never

**Category:** RSA / Padding · **Points:** 100

**Challenge files:** [`output.txt`](output.txt), [`pad_encrypt.py`](pad_encrypt.py)

## Idea

Padding with null bytes just multiplies the message: `m = FLAG * 256^57`. So `FLAG^3 ≡ c / 256^171 (mod n)`.
The 43-byte flag cubed is only a little larger than the 1024-bit `n`, so `FLAG^3 = f3 + t*n` for a small `t`; brute force `t` until we get a perfect cube.

## Solution

```python
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
```

## Flag

```text
crypto{n0n_574nd4rd_p4d_c0n51d3r3d_h4rmful}
```
