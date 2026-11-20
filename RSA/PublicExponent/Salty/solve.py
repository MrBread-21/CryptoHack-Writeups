from Crypto.Util.number import long_to_bytes

exec(open("output.txt").read())  # n, e = 1, ct
print(long_to_bytes(ct))  # m^1 mod n = m
#crypto{saltstack_fell_for_this!}
