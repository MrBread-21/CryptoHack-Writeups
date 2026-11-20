# Chinese Remainder Theorem

**Category:** Mathematics / Modular Math · **Points:** 40

## Idea

Chinese Remainder Theorem with pairwise coprime moduli 5, 11, 17 gives a unique solution modulo 935. SymPy's `crt(moduli, residues)` solves it.

## Solution

```python
from sympy.ntheory.modular import crt

print(crt([5, 11, 17], [2, 3, 5])[0])
#872
```

## Flag

```text
872
```
