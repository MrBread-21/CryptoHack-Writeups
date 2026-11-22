from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read().replace(":", " ="))  # n, e, c

# p, q are Mersenne primes 2^k - 1 -> just try every k
for k in range(2, 10000):
    p = 2 ** k - 1
    if n % p == 0:
        q = n // p
        print(long_to_bytes(pow(c, pow(e, -1, (p - 1) * (q - 1)), n)))
        break
#crypto{Th3se_Pr1m3s_4r3_t00_r4r3}
