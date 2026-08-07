# Pwntools Example

![Network Attacks](challenge.jpg)

## Description

The challenge introduces basic network interaction using the `pwntools` library. A server is running on `socket.cryptohack.org:11112` and communicates exclusively through JSON messages.

Our objective is to send a JSON object requesting to buy the flag.

## Analysis

After connecting to the server, it displays the following banner:

```text
Welcome to netcat's flag shop!
What would you like to buy?
I only speak JSON, I hope that's ok.
```

The challenge description specifies that the server expects the following JSON object:

```json
{
    "buy": "flag"
}
```

Using `pwntools`, we establish a TCP connection, serialize the request with Python's `json` module, send it to the server, and parse the JSON response.

## Solution

```python
from pwn import *
import json

HOST = "socket.cryptohack.org"
PORT = 11112

conn = remote(HOST, PORT)

# Read the banner
for _ in range(4):
    print(conn.recvline().decode(), end="")

request = {
    "buy": "flag"
}

conn.sendline(json.dumps(request).encode())

response = json.loads(conn.recvline().decode())
print(response)

conn.close()
```

Output:

```text
{'flag': 'crypto{sh0pp1ng_f0r_fl4g5}'}
```

## Flag

```text
crypto{sh0pp1ng_f0r_fl4g5}
```

## Takeaways

- `pwntools` simplifies TCP communication for CTF challenges.
- Many CryptoHack network challenges exchange data using JSON.
- The `json` module can be used to serialize Python dictionaries before sending them over the network and parse JSON responses from the server.