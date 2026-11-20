# Modulus Inutilis

**Category:** RSA / Public exponent · **Points:** 50

**Challenge files:** [`modulus_inutilis.py`](modulus_inutilis.py), [`output.txt`](output.txt)

## Idea

`e = 3` and the flag is short, so `m^3 < n` and no modular reduction happens. The integer cube root of `ct` is `m`.

## Solution

```python
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e = 3, ct
# m^3 < n -> no modular reduction happened, just take the integer cube root
print(long_to_bytes(int(iroot(ct, 3)[0])))
#crypto{N33d_m04R_p4dd1ng}
```

## Flag

```text
crypto{N33d_m04R_p4dd1ng}
```
