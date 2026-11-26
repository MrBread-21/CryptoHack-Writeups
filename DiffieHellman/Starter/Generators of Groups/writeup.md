# Generators of Groups

**Category:** Diffie-Hellman / Starter · **Points:** 20

## Idea

`g` generates `F_p*` iff its order is `p - 1`, i.e. `g^((p-1)/q) != 1` for every prime factor `q` of `p - 1`. Test `g = 2, 3, ...` and print the first one.

## Solution

```python
from sympy import primefactors

p = 28151
# g is primitive iff g^((p-1)/q) != 1 for every prime q | p - 1
for g in range(2, p):
    if all(pow(g, (p - 1) // q, p) != 1 for q in primefactors(p - 1)):
        print(g)
        break
#7
```

## Flag

```text
7
```
