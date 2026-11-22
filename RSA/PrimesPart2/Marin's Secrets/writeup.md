# Marin's Secrets

**Category:** RSA / Primes Part 2 · **Points:** 50

**Challenge files:** [`marin.py`](marin.py), [`output.txt`](output.txt)

## Idea

Both primes are Mersenne primes `2^k - 1`. There are very few of them, so try every `k` until `2^k - 1` divides `n`.

## Solution

```python
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read().replace(":", " ="))  # n, e, c

# p, q are Mersenne primes 2^k - 1 -> just try every k
for k in range(2, 10000):
    p = 2 ** k - 1
    if n % p == 0:
        q = n // p
        print(long_to_bytes(pow(c, pow(e, -1, (p - 1) * (q - 1)), n)))
        break
#crypto{Th3se_Pr1m3s_4r3_t00_r4r3}
```

## Flag

```text
crypto{Th3se_Pr1m3s_4r3_t00_r4r3}
```
