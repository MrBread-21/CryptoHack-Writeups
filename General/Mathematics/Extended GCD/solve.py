def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = egcd(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = egcd(26513, 32321)
print(u, v, min(u, v))
#-8404
