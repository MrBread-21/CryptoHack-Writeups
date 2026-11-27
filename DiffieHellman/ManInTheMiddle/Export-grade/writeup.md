# Export-grade

**Category:** Diffie-Hellman / Man In The Middle · **Points:** 100

## Idea

We intercept the negotiation and tell Bob that Alice only supports `DH64`. With a 64-bit prime the discrete log of `A` is easy (`sympy.discrete_log`, Pohlig-Hellman / Pollard), giving `a` and the shared secret.

## Solution

```python
from pwn import remote
import json, sys
from sympy.ntheory import discrete_log
sys.path.append("../../Starter/Deriving Symmetric Keys")
from decrypt import decrypt_flag

r = remote("socket.cryptohack.org", 13379)
recv = lambda: json.loads(r.recvuntil(b"}").split(b": ", 1)[1])

recv()
r.sendlineafter(b"Bob: ", json.dumps({"supported": ["DH64"]}).encode())   # downgrade!
recv()
r.sendlineafter(b"Alice: ", json.dumps({"chosen": "DH64"}).encode())
params, B, msg = recv(), recv(), recv()
p, g, A, B = [int(x, 16) for x in (params["p"], params["g"], params["A"], B["B"])]

a = discrete_log(p, A, g)  # 64-bit DLP is easy
print(decrypt_flag(pow(B, a, p), msg["iv"], msg["encrypted_flag"]))
#crypto{d0wn6r4d35_4r3_d4n63r0u5}
```

## Flag

```text
crypto{d0wn6r4d35_4r3_d4n63r0u5}
```
