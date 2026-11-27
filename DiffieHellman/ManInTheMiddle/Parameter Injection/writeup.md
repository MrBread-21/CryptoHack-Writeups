# Parameter Injection

**Category:** Diffie-Hellman / Man In The Middle · **Points:** 60

## Idea

As a man-in-the-middle we can rewrite Bob's public key. Send Alice `B = p`: her shared secret becomes `p^a mod p = 0`, so we know the AES key derived from `0`.

## Solution

```python
from pwn import remote
import json, sys
sys.path.append("../../Starter/Deriving Symmetric Keys")
from decrypt import decrypt_flag

r = remote("socket.cryptohack.org", 13371)
recv = lambda: json.loads(r.recvuntil(b"}").split(b": ", 1)[1])

alice = recv()
r.sendlineafter(b"Bob: ", json.dumps(alice).encode())          # forward Alice -> Bob
bob = recv()
r.sendlineafter(b"Alice: ", json.dumps({"B": alice["p"]}).encode())  # B = p  ->  Alice's secret = p^a mod p = 0
msg = recv()
print(decrypt_flag(0, msg["iv"], msg["encrypted_flag"]))
#crypto{n1c3_0n3_m4ll0ry!!!!!!!!}
```

## Flag

```text
crypto{n1c3_0n3_m4ll0ry!!!!!!!!}
```
