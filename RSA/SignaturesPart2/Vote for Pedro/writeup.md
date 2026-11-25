# Vote for Pedro

**Category:** RSA / Signatures Part 2 · **Points:** 150

**Challenge files:** [`13375.py`](13375.py), [`alice.key`](alice.key)

## Idea

Alice's `e = 3` and the server only checks what comes after the last `\x00`. We need `x^3` to *end* with `\x00VOTE FOR PEDRO` (15 bytes).
Solve `x^3 ≡ target (mod 2^120)` bit by bit (Hensel lifting, works because the target is odd). Then `x < 2^120`, so `x^3 < N`: no reduction, the low bytes are exactly our target.

## Solution

```python
from pwn import remote
import json
from Crypto.Util.number import bytes_to_long

# Alice uses e = 3 and the server only checks the bytes after the last \x00.
# Find x with x^3 = b"\x00VOTE FOR PEDRO" (mod 2^120): then x^3 < N, no reduction happens.
target = bytes_to_long(b"\x00VOTE FOR PEDRO")
x = 1
for k in range(1, 121):          # lift the cube root bit by bit (Hensel)
    if pow(x, 3, 2 ** k) != target % 2 ** k:
        x += 2 ** (k - 1)
assert pow(x, 3, 2 ** 120) == target

r = remote("socket.cryptohack.org", 13375)
r.recvline()
r.sendline(json.dumps({"option": "vote", "vote": hex(x)}).encode())
print(r.recvline())
#crypto{y0ur_v0t3_i5_my_v0t3}
```

## Flag

```text
crypto{y0ur_v0t3_i5_my_v0t3}
```
