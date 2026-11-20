# Greatest Common Divisor

**Category:** General / Mathematics · **Points:** 15

## Idea

Euclid's algorithm: `gcd(a, b) = gcd(b, a mod b)` until `b = 0`.

## Solution

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(66528, 52920))
#1512
```

## Flag

```text
1512
```
