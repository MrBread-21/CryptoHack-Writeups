# Roll your Own

**Category:** Mathematics / Brainteasers Part 2 · **Points:** 125

**Challenge files:** [`13403.py`](13403.py)

## Idea

We choose `n` and `g` freely as long as `g^q ≡ 1 (mod n)`. Take `n = q^2`, `g = 1 + q` (Paillier trick):
`(1 + q)^x ≡ 1 + x*q (mod q^2)` by the binomial theorem, so `g^q ≡ 1` and the discrete log is just `x = (h - 1) / q`.

## Solution

```python
from pwn import remote
import json

r = remote("socket.cryptohack.org", 13403)
q = int(r.recvline().split(b": ")[1].strip().strip(b'"'), 16)

# n = q^2, g = 1 + q  ->  g^x = 1 + x*q (mod q^2)  (binomial theorem), and g^q = 1
r.sendline(json.dumps({"g": hex(1 + q), "n": hex(q * q)}).encode())
h = int(r.recvline().split(b": ")[-1].strip().strip(b'"'), 16)
r.sendline(json.dumps({"x": hex((h - 1) // q)}).encode())
print(r.recvline())
#crypto{Grabbing_Flags_with_Pascal_Paillier}
```

## Flag

```text
crypto{Grabbing_Flags_with_Pascal_Paillier}
```
