from sympy import isprime

xs = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

for p in range(max(xs) + 1, 1000):
    if isprime(p):
        x = xs[1] * pow(xs[0], -1, p) % p
        if all(xs[i] * x % p == xs[i + 1] for i in range(len(xs) - 1)):
            print(f"crypto{{{p},{x}}}")
#crypto{919,209}
