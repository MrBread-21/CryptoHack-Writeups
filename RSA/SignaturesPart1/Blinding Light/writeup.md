# Blinding Light

**Category:** RSA / Signatures Part 1 · **Points:** 120

**Challenge files:** [`13376.py`](13376.py)

## Idea

RSA is multiplicative. Ask for a signature of `m' = m * 2^e` (which does not contain `admin=True`): `m'^d = m^d * 2`. Divide by 2 modulo `N` to get a valid signature for `admin=True`.

## Solution

```python
from pwn import remote
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote("socket.cryptohack.org", 13376)
r.recvline()

def send(d):
    r.sendline(json.dumps(d).encode())
    return json.loads(r.recvline())

key = send({"option": "get_pubkey"})
N, e = int(key["N"], 16), int(key["e"], 16)
m = bytes_to_long(b"admin=True")

# Blind signature: sign m * 2^e instead, then divide the signature by 2
blinded = m * pow(2, e, N) % N
s = int(send({"option": "sign", "msg": long_to_bytes(blinded).hex()})["signature"], 16)
s = s * pow(2, -1, N) % N
print(send({"option": "verify", "msg": long_to_bytes(m).hex(), "signature": hex(s)}))
#crypto{m4ll34b1l17y_c4n_b3_d4n63r0u5}
```

## Flag

```text
crypto{m4ll34b1l17y_c4n_b3_d4n63r0u5}
```
