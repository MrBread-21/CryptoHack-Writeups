# Salty

**Category:** RSA / Public exponent · **Points:** 20

**Challenge files:** [`output.txt`](output.txt), [`salty.py`](salty.py)

## Idea

With `e = 1`, "encryption" does nothing: `ct = m^1 mod n = m`. Just convert `ct` to bytes.

## Solution

```python
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e = 1, ct
print(long_to_bytes(ct))  # m^1 mod n = m
#crypto{saltstack_fell_for_this!}
```

## Flag

```text
crypto{saltstack_fell_for_this!}
```
