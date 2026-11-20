# Inferius Prime

**Category:** RSA / Primes Part 1 · **Points:** 30

**Challenge files:** [`inferius.py`](inferius.py), [`output.txt`](output.txt)

## Idea

The author confused bits and bytes: the primes are only 100 bits, so `n` is ~200 bits and factors immediately. Then compute `d` and decrypt.

## Solution

```python
from sympy import factorint
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, ct
p, q = factorint(n)  # n is only ~200 bits -> easy to factor
d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(ct, d, n)))
#crypto{N33d_b1g_pR1m35}
```

## Flag

```text
crypto{N33d_b1g_pR1m35}
```
