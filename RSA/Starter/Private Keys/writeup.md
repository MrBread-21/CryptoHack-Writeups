# Private Keys

**Category:** RSA / Starter · **Points:** 20

## Idea

The private exponent is `d = e^-1 mod phi(N)`; Python 3.8+ computes it with `pow(e, -1, phi)`.

## Solution

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
print(pow(e, -1, (p - 1) * (q - 1)))
#121832886702415731577073962957377780195510499965398469843281
```

## Flag

```text
121832886702415731577073962957377780195510499965398469843281
```
