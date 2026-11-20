a, p = 288260533169915, 1007621497415251
ct = eval(open("output.txt").read())

# a is a quadratic residue and p = 3 mod 4 (so -1 is NOT a residue):
# a^e is always a residue, -a^e is never -> Legendre symbol reveals each bit
bits = "".join("1" if pow(n, (p - 1) // 2, p) == 1 else "0" for n in ct)
print(int(bits, 2).to_bytes(len(bits) // 8, "big"))
#crypto{p4tterns_1n_re5idu3s}
