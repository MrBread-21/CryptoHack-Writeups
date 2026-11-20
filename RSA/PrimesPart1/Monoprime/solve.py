from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e, ct
# n is prime -> phi(n) = n - 1
d = pow(e, -1, n - 1)
print(long_to_bytes(pow(ct, d, n)))
#crypto{0n3_pr1m3_41n7_pr1m3_l0l}
