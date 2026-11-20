import requests
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # N, e, c

# Intended: Boneh-Durfee (d < N^0.292). Shortcut: N is already factored on factordb
p, q = [int(f[0]) for f in requests.get("http://factordb.com/api", params={"query": N}).json()["factors"]]
d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(c, d, N)))
#crypto{bon3h5_4tt4ck_i5_sr0ng3r_th4n_w13n3r5}
