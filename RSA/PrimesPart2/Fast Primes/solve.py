import requests
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

key = RSA.import_key(open("key.pem").read())
ct = bytes.fromhex(open("ciphertext.txt").read())

# Intended: ROCA (p = k*M + 65537^a mod M). Shortcut: the 512-bit n is factored on factordb
p, q = [int(f[0]) for f in requests.get("http://factordb.com/api", params={"query": key.n}).json()["factors"]]
d = pow(key.e, -1, (p - 1) * (q - 1))
priv = RSA.construct((key.n, key.e, d, p, q))
print(PKCS1_OAEP.new(priv).decrypt(ct))
#crypto{p00R_3570n14}
