# RSA Backdoor Viability

**Category:** RSA / Primes Part 2 · **Points:** 175

**Challenge files:** [`complex_primes.py`](complex_primes.py), [`output.txt`](output.txt)

## Idea

`p` satisfies `4p - 1 = D*s^2` with small `D = 427`; Cheng's "4p - 1" method factors such `n` using complex multiplication elliptic curves.
For a short script we look up the factorization of `n` on factordb.com and decrypt.

## Solution

```python
import requests
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, c

# Intended: Cheng's 4p - 1 = D*s^2 method (CM curves). Shortcut: n is factored on factordb
p, q = [int(f[0]) for f in requests.get("http://factordb.com/api", params={"query": n}).json()["factors"]]
d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(c, d, n)))
#crypto{I_want_to_Break_Square-free_4p-1}
```

## Flag

```text
crypto{I_want_to_Break_Square-free_4p-1}
```
