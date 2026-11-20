# Unencryptable

**Category:** Mathematics / Brainteasers Part 2 · **Points:** 125

**Challenge files:** [`output.txt`](output.txt), [`source.py`](source.py)

## Idea

`DATA` is a fixed point: `DATA^e ≡ DATA (mod N)`, so `DATA^(e-1) = DATA^(2^16) ≡ 1`.
Squaring `DATA` repeatedly we reach 1; the value just before is a square root of 1 that is not `±1`, hence `gcd(x - 1, N)` is a prime factor of `N`. Then decrypt normally.

## Solution

```python
from math import gcd
from Crypto.Util.number import bytes_to_long, long_to_bytes

DATA = bytes_to_long(bytes.fromhex(open("source.py").read().split('fromhex("')[1].split('"')[0]))
exec(open("output.txt").read().split("RSA broken!?")[1])  # N, e, c

# DATA^e = DATA  ->  DATA^(2^16) = 1 (mod N).  Square repeatedly until we hit 1:
# the value x before that is a non-trivial square root of 1, so gcd(x - 1, N) = p
x = DATA
while pow(x, 2, N) != 1:
    x = pow(x, 2, N)
p = gcd(x - 1, N)
q = N // p
d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(c, d, N)))
#crypto{R3m3mb3r!_F1x3d_P0iNts_aR3_s3crE7s_t00}
```

## Flag

```text
crypto{R3m3mb3r!_F1x3d_P0iNts_aR3_s3crE7s_t00}
```
