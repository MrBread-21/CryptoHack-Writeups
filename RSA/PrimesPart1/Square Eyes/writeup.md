# Square Eyes

**Category:** RSA / Primes Part 1 · **Points:** 35

**Challenge files:** [`output.txt`](output.txt)

## Idea

`n = p^2`, so `p = isqrt(n)`. Careful: `phi(p^2) = p(p - 1)`, not `(p - 1)^2`.

## Solution

```python
from math import isqrt
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, ct
p = isqrt(n)  # n = p^2  ->  phi(n) = p * (p - 1)
d = pow(e, -1, p * (p - 1))
print(long_to_bytes(pow(ct, d, n)))
#crypto{squar3_r00t_i5_f4st3r_th4n_f4ct0r1ng!}
```

## Flag

```text
crypto{squar3_r00t_i5_f4st3r_th4n_f4ct0r1ng!}
```
