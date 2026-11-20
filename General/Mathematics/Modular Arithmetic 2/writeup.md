# Modular Arithmetic 2

**Category:** General / Mathematics · **Points:** 20

## Idea

Fermat's little theorem: for prime `p` and `a` not divisible by `p`, `a^(p-1) ≡ 1 (mod p)`. Here `p = 65537`, exponent `65536 = p - 1`, so the answer is `1`.

## Solution

```python
# Fermat's little theorem: a^(p-1) = 1 mod p
print(pow(273246787654, 65536, 65537))
#1
```

## Flag

```text
1
```
