# Adrien's Signs

**Category:** Mathematics / Brainteasers Part 1 · **Points:** 80

**Challenge files:** [`output.txt`](output.txt), [`source.py`](source.py)

## Idea

`a` is a quadratic residue mod `p`, so every `a^e` is a residue. Since `p ≡ 3 (mod 4)`, `-1` is a non-residue, hence `-a^e` is a non-residue.
So the Legendre symbol of each ciphertext number tells us the bit: residue -> `1`, non-residue -> `0`.

## Solution

```python
a, p = 288260533169915, 1007621497415251
ct = eval(open("output.txt").read())

# a is a quadratic residue and p = 3 mod 4 (so -1 is NOT a residue):
# a^e is always a residue, -a^e is never -> Legendre symbol reveals each bit
bits = "".join("1" if pow(n, (p - 1) // 2, p) == 1 else "0" for n in ct)
print(int(bits, 2).to_bytes(len(bits) // 8, "big"))
#crypto{p4tterns_1n_re5idu3s}
```

## Flag

```text
crypto{p4tterns_1n_re5idu3s}
```
