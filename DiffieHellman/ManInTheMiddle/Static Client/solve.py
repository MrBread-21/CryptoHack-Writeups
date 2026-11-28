from pwn import remote
import json, sys
sys.path.append("../../Starter/Deriving Symmetric Keys")
from decrypt import decrypt_flag

r = remote("socket.cryptohack.org", 13373)
recv = lambda: json.loads(r.recvuntil(b"}").split(b": ", 1)[1])

alice, bob, msg = recv(), recv(), recv()
# Bob reuses his secret b. Send him g = A: his "public key" becomes A^b = the shared secret!
r.sendlineafter(b"parameters: ", json.dumps({"p": alice["p"], "g": alice["A"], "A": "0x01"}).encode())
shared = int(recv()["B"], 16)
print(decrypt_flag(shared, msg["iv"], msg["encrypted"]))
#crypto{n07_3ph3m3r4l_3n0u6h}
