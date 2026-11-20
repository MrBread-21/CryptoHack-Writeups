# Everything is Still Big

**Category:** RSA / Public exponent · **Points:** 100

**Challenge files:** [`output.txt`](output.txt), [`source.py`](source.py)

## Idea

`d` is 512 bits, just above Wiener's bound, but below the Boneh-Durfee bound `d < N^0.292`, so the intended solution is the Boneh-Durfee lattice attack.
To keep the code short we use the fact that this `N` is already factored on factordb.com, then decrypt normally.

## Solution

```python
import requests
from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # N, e, c

# Intended: Boneh-Durfee (d < N^0.292). Shortcut: N is already factored on factordb
p, q = [int(f[0]) for f in requests.get("http://factordb.com/api", params={"query": N}).json()["factors"]]
d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(c, d, N)))
#crypto{bon3h5_4tt4ck_i5_sr0ng3r_th4n_w13n3r5}
```

## Flag

```text
crypto{bon3h5_4tt4ck_i5_sr0ng3r_th4n_w13n3r5}
```
