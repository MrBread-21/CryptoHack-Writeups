# Modular Arithmetic 1

**Category:** General / Mathematics · **Points:** 20

## Idea

Just reduce both numbers: `11 mod 6 = 5`, `8146798528947 mod 17 = 4`. The smaller one is `4`.

## Solution

```python
x = 11 % 6
y = 8146798528947 % 17
print(min(x, y))
#4
```

## Flag

```text
4
```
