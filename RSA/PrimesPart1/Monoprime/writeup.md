# Monoprime

**Category:** RSA / Primes Part 1 · **Points:** 30

**Challenge files:** [`output.txt`](output.txt)

## Idea

`n` itself is prime, so `phi(n) = n - 1` and anyone can compute `d = e^-1 mod (n - 1)`.

## Solution

```python
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, ct
# n is prime -> phi(n) = n - 1
d = pow(e, -1, n - 1)
print(long_to_bytes(pow(ct, d, n)))
#crypto{0n3_pr1m3_41n7_pr1m3_l0l}
```

## Flag

```text
crypto{0n3_pr1m3_41n7_pr1m3_l0l}
```
