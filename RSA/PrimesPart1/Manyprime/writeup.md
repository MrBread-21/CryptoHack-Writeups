# Manyprime

**Category:** RSA / Primes Part 1 · **Points:** 40

**Challenge files:** [`output.txt`](output.txt)

## Idea

`n` is the product of ~30 small (64-bit) primes. ECM finds small factors fast regardless of `n`'s size; FLINT's `fmpz.factor()` does it in about a minute.
`phi(n) = prod(p_i - 1)`, then decrypt.

## Solution

```python
from flint import fmpz
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, ct
# ~30 small primes -> FLINT's factor() (uses ECM) splits n in seconds
phi = 1
for p, _ in fmpz(n).factor():
    phi *= int(p) - 1
print(long_to_bytes(pow(ct, pow(e, -1, phi), n)))
#crypto{700_m4ny_5m4ll_f4c70r5}
```

## Flag

```text
crypto{700_m4ny_5m4ll_f4c70r5}
```
