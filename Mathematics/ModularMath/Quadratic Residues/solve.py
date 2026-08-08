#!/usr/bin/env python3

p = 29

values = [14, 6, 19]

for x in values:
    roots = [
        a for a in range(1, p)
        if a * a % p == x
    ]

    if roots:
        print(f"Quadratic residue: {x}")
        print(f"Roots: {roots}")
        print(f"Number: {min(roots)}")