# Ellipse Curve Cryptography

**Category:** Mathematics / Brainteasers Part 2 · **Points:** 125

**Challenge files:** [`output.txt`](output.txt), [`source.py`](source.py)

## Idea

The "curve" is the Pell conic `x^2 - D*y^2 = 1` and the addition law is multiplication of `x + y*sqrt(D)`.
Here `D = 529 = 23^2` is a perfect square, so the map `(x, y) -> x + 23*y (mod p)` is a group isomorphism into `F_p*`.
The discrete log becomes a normal DLP in `F_p*` (`p - 1` is smooth -> Pohlig-Hellman via `sympy.discrete_log`).
With Alice's secret `n_a`, the shared x-coordinate is `(b^n_a + b^-n_a) / 2` where `b = x_B + 23*y_B`.

## Solution

```python
from hashlib import sha1
from Crypto.Cipher import AES
from sympy.ntheory import discrete_log

p = 173754216895752892448109692432341061254596347285717132408796456167143559
D = 529  # = 23^2
G = (29394812077144852405795385333766317269085018265469771684226884125940148,
     94108086667844986046802106544375316173742538919949485639896613738390948)
A = (155781055760279718382374741001148850818103179141959728567110540865590463,
     73794785561346677848810778233901832813072697504335306937799336126503714)
B = (171226959585314864221294077932510094779925634276949970785138593200069419,
     54353971839516652938533335476115503436865545966356461292708042305317630)
iv = "64bc75c8b38017e1397c46f85d4e332b"
enc = "13e4d200708b786d8f7c3bd2dc5de0201f0d7879192e6603d7c5d6b963e1df2943e3ff75f7fda9c30a92171bbbc5acbf"

# x^2 - 23^2 y^2 = (x - 23y)(x + 23y) = 1, and the "point addition" is just
# multiplication of (x + 23y) in F_p  ->  the ECDLP becomes a normal DLP in F_p*
f = lambda P: (P[0] + 23 * P[1]) % p
n_a = discrete_log(p, f(A), f(G))

# shared.x = (b^n + b^-n) / 2  with  b = x_B + 23 y_B
b = pow(f(B), n_a, p)
shared = (b + pow(b, -1, p)) * pow(2, -1, p) % p

key = sha1(str(shared).encode()).digest()[:16]
print(AES.new(key, AES.MODE_CBC, bytes.fromhex(iv)).decrypt(bytes.fromhex(enc)))
#crypto{c0n1c_s3ct10n5_4r3_f1n1t3_gr0up5}
```

## Flag

```text
crypto{c0n1c_s3ct10n5_4r3_f1n1t3_gr0up5}
```
