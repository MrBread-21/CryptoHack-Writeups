# Public Keys

**Category:** RSA / Starter · **Points:** 15

## Idea

RSA encryption: `c = m^e mod N` with `N = p*q = 391`.

## Solution

```python
p, q, e = 17, 23, 65537
print(pow(12, e, p * q))
#301
```

## Flag

```text
301
```
