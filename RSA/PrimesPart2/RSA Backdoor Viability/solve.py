import requests
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, c

# Intended: Cheng's 4p - 1 = D*s^2 method (CM curves). Shortcut: n is factored on factordb
p, q = [int(f[0]) for f in requests.get("http://factordb.com/api", params={"query": n}).json()["factors"]]
d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(c, d, n)))
#crypto{I_want_to_Break_Square-free_4p-1}
