# Encoding Challenge

**Category:** General / Encoding · **Points:** 40

**Challenge files:** [`13377.py`](13377.py), [`pwntools_example.py`](pwntools_example.py)

## Idea

The server sends 100 JSON messages, each with an `encoding` type (`base64`, `hex`, `rot13`, `bigint`, `utf-8`) and the encoded data.
Keep a dictionary `type -> decode function`, decode every message and send back `{"decoded": ...}`. After 100 levels the server returns the flag.

## Solution

```python
from pwn import remote
import json, base64, codecs
from Crypto.Util.number import long_to_bytes

decode = {
    "base64": lambda x: base64.b64decode(x).decode(),
    "hex":    lambda x: bytes.fromhex(x).decode(),
    "rot13":  lambda x: codecs.decode(x, "rot13"),
    "bigint": lambda x: long_to_bytes(int(x, 16)).decode(),
    "utf-8":  lambda x: "".join(map(chr, x)),
}

r = remote("socket.cryptohack.org", 13377)
for _ in range(100):
    msg = json.loads(r.recvline())
    r.sendline(json.dumps({"decoded": decode[msg["type"]](msg["encoded"])}).encode())
print(json.loads(r.recvline())["flag"])
#crypto{3nc0d3_d3c0d3_3nc0d3}
```

## Flag

```text
crypto{3nc0d3_d3c0d3_3nc0d3}
```
