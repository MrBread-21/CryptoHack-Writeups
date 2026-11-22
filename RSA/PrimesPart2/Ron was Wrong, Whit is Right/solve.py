import zipfile
from math import gcd
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

z = zipfile.ZipFile("keys_and_messages.zip")
keys = {i: RSA.import_key(z.read(f"keys_and_messages/{i}.pem")) for i in range(1, 51)}

# Some keys share a prime factor (bad RNG) -> gcd of two moduli reveals it
for i in keys:
    for j in keys:
        p = gcd(keys[i].n, keys[j].n)
        if i != j and p > 1:
            n, e = keys[i].n, keys[i].e
            q = n // p
            priv = RSA.construct((n, e, pow(e, -1, (p - 1) * (q - 1)), p, q))
            ct = bytes.fromhex(z.read(f"keys_and_messages/{i}.ciphertext").decode())
            print(PKCS1_OAEP.new(priv).decrypt(ct))
            raise SystemExit
#crypto{3ucl1d_w0uld_b3_pr0ud}
