import math
from decimal import Decimal, getcontext
from flint import fmpz_mat

getcontext().prec = 100
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
ct = 1350995397927355657956786955603012410260017344805998076702828160316695004588429433
n = 23  # len("crypto{???????????????}")

# ct ~ sum(c_i * floor(sqrt(p_i) * 16^64))  -> knapsack, solve with LLL
s = [math.floor(Decimal(p).sqrt() * 16**64) for p in PRIMES[:n]]
rows = [[int(i == j) for j in range(n)] + [s[i]] for i in range(n)]
rows.append([0] * n + [-ct])
L = fmpz_mat(rows).lll()

for i in range(L.nrows()):
    v = [int(L[i, j]) for j in range(n)]
    if all(32 <= abs(x) < 127 for x in v) and len(set(x > 0 for x in v)) == 1:
        print("".join(chr(abs(x)) for x in v))
#crypto{r34l_t0_23D_m4p}
