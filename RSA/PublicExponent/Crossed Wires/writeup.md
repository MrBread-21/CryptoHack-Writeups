# Crossed Wires

**Category:** RSA / Public exponent · **Points:** 100

**Challenge files:** [`output.txt`](output.txt), [`source.py`](source.py)

## Idea

We know our own `(N, d)`. From `e*d - 1 = k*phi` we can factor `N` (find a non-trivial square root of 1, like Miller-Rabin).
All friends use the same `N`, so the flag is `m^(e1*e2*e3*e4*e5) mod N`; invert the product of exponents modulo `phi`.

## Solution

```python
import random
from math import gcd
from Crypto.Util.number import long_to_bytes

lines = open("output.txt").read().splitlines()
N, d = eval(lines[0].split(": ")[1])
friends = eval(lines[1].split(": ")[1])
c = int(lines[2].split(": ")[1])
e = 0x10001

# 1. Factor N from (e, d): e*d - 1 = k*phi, find a non-trivial square root of 1
k = e * d - 1
t = k
while t % 2 == 0:
    t //= 2
while True:
    x = pow(random.randrange(2, N), t, N)
    while pow(x, 2, N) != 1:
        x = pow(x, 2, N)
    p = gcd(x - 1, N)
    if 1 < p < N:
        break
phi = (p - 1) * (N // p - 1)

# 2. All friends share N, so c = m^(e1*e2*...*e5)  ->  invert the product
E = 1
for _, ei in friends:
    E *= ei
print(long_to_bytes(pow(c, pow(E, -1, phi), N)))
#crypto{3ncrypt_y0ur_s3cr3t_w1th_y0ur_fr1end5_publ1c_k3y}
```

## Flag

```text
crypto{3ncrypt_y0ur_s3cr3t_w1th_y0ur_fr1end5_publ1c_k3y}
```
