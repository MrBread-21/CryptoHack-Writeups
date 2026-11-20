# Factoring

**Category:** RSA / Primes Part 1 · **Points:** 15

## Idea

A 150-bit number is tiny; `sympy.factorint` factors it instantly.

## Solution

```python
from sympy import factorint

print(min(factorint(510143758735509025530880200653196460532653147)))
#19704762736204164635843
```

## Flag

```text
19704762736204164635843
```
