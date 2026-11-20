from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt

exec(open("out.txt").read())  # p, q, vka, vkakb, vkb, c
n = p * q

# v = p*r  ->  v = 0 (mod p).  Mod q everything is invertible:
# v = vka * vkb / vkakb (mod q)
vq = vka * vkb * pow(vkakb, -1, q) % q
v = int(crt([p, q], [0, vq])[0])

key = sha256(long_to_bytes(v)).digest()
print(AES.new(key, AES.MODE_ECB).decrypt(bytes.fromhex(c)))
#crypto{1nv3rt1bl3_k3y_3xch4ng3_pr0t0c0l}
