# Infinite Descent

**Category:** RSA / Primes Part 2 · **Points:** 50

**Challenge files:** [`descent.py`](descent.py), [`output.txt`](output.txt)

## Idea

`p` and `q` start from the same random number and differ only by small increments, so `|p - q|` is tiny.
Fermat factorization: start at `a = ceil(sqrt(n))` and increase until `a^2 - n` is a perfect square `b^2`; then `p, q = a ± b`.

## Solution

```python
from gmpy2 import isqrt, is_square
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, c

# p and q are very close -> Fermat factorization: n = a^2 - b^2
a = isqrt(n) + 1
while not is_square(a * a - n):
    a += 1
b = isqrt(a * a - n)
p, q = a + b, a - b
print(long_to_bytes(pow(c, pow(e, -1, (p - 1) * (q - 1)), n)))
#crypto{f3rm47_w45_4_g3n1u5}
```

## Flag

```text
crypto{f3rm47_w45_4_g3n1u5}
```
