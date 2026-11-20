# Extended GCD

**Category:** General / Mathematics · **Points:** 20

## Idea

The extended Euclidean algorithm returns `u, v` with `p*u + q*v = gcd(p, q) = 1` (p, q are primes).
Recursively: if `g = b*u' + (a mod b)*v'` then `u = v'`, `v = u' - (a // b) * v'`. The smaller of `u, v` is the flag.

## Solution

```python
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = egcd(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = egcd(26513, 32321)
print(u, v, min(u, v))
#-8404
```

## Flag

```text
-8404
```
