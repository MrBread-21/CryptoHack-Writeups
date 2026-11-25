# Working with Fields

**Category:** Diffie-Hellman / Starter · **Points:** 10

## Idea

In `F_p` every non-zero element has an inverse. Python computes it with `pow(g, -1, p)` (or `g^(p-2)` by Fermat's little theorem).

## Solution

```python
p, g = 991, 209
print(pow(g, -1, p))  # or pow(g, p - 2, p) by Fermat
#569
```

## Flag

```text
569
```
