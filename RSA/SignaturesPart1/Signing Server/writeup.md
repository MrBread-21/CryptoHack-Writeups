# Signing Server

**Category:** RSA / Signatures Part 1 · **Points:** 60

**Challenge files:** [`13374.py`](13374.py)

## Idea

Textbook RSA signing is the same operation as decryption: `sign(c) = c^d mod N`. Ask the server to "sign" the encrypted secret and it decrypts it for us.

## Solution

```python
from pwn import remote
import json
from Crypto.Util.number import long_to_bytes

r = remote("socket.cryptohack.org", 13374)
r.recvline()

def send(d):
    r.sendline(json.dumps(d).encode())
    return json.loads(r.recvline())

# "signing" is decryption: sign(c) = c^d = m
secret = send({"option": "get_secret"})["secret"]
print(long_to_bytes(int(send({"option": "sign", "msg": secret})["signature"], 16)))
#crypto{d0n7_516n_ju57_4ny7h1n6}
```

## Flag

```text
crypto{d0n7_516n_ju57_4ny7h1n6}
```
