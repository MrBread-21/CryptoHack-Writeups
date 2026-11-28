from pwn import remote
import json, sys
sys.path.append("../../Starter/Deriving Symmetric Keys")
from decrypt import decrypt_flag

r = remote("socket.cryptohack.org", 13380)
recv = lambda: json.loads(r.recvuntil(b"}").split(b": ", 1)[1])

alice, bob, msg = recv(), recv(), recv()
p, g, A, B = [int(x, 16) for x in (alice["p"], alice["g"], alice["A"], bob["B"])]

# Additive group: A = a*g (mod p), so the "discrete log" is just a division
a = A * pow(g, -1, p) % p
print(decrypt_flag(a * B % p, msg["iv"], msg["encrypted"]))
#crypto{cycl1c_6r0up_und3r_4dd1710n?}
