# Modular Inverting

**Category:** General / Mathematics · **Points:** 25

## Idea

From Fermat's little theorem `a^(p-1) ≡ 1`, so `a * a^(p-2) ≡ 1`, i.e. `a^-1 ≡ a^(p-2) (mod p)`. `3^11 mod 13 = 9`.

## Solution

```python
# Fermat: a^(p-2) = a^-1 mod p
print(pow(3, 13 - 2, 13))  # or pow(3, -1, 13)
#9
```

## Flag

```text
9
```
