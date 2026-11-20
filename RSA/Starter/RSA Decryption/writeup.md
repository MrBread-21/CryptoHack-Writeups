# RSA Decryption

**Category:** RSA / Starter · **Points:** 20

## Idea

Decryption: `m = c^d mod N`, using `d` from the previous challenge.

## Solution

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
N, e = p * q, 65537
c = 77578995801157823671636298847186723593814843845525223303932

d = pow(e, -1, (p - 1) * (q - 1))
print(pow(c, d, N))
#13371337
```

## Flag

```text
13371337
```
