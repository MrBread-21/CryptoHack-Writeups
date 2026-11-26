from sympy import primefactors

p = 28151
# g is primitive iff g^((p-1)/q) != 1 for every prime q | p - 1
for g in range(2, p):
    if all(pow(g, (p - 1) // q, p) != 1 for q in primefactors(p - 1)):
        print(g)
        break
#7
