# Lemur XOR

**Category:** General / XOR · **Points:** 40

**Challenge files:** [`flag.png`](flag.png), [`lemur.png`](lemur.png), [`xor.png`](xor.png)

## Idea

Both images were XORed with the same key: `lemur ^ key` and `flag ^ key`.
XORing them together cancels the key: `(lemur ^ key) ^ (flag ^ key) = lemur ^ flag`, so the flag text becomes visible.
We XOR the RGB pixel bytes (not the raw file bytes) and save the result as `xor.png`.

## Solution

```python
from PIL import Image

a = Image.open("lemur.png").convert("RGB")
b = Image.open("flag.png").convert("RGB")
out = Image.frombytes("RGB", a.size, bytes(x ^ y for x, y in zip(a.tobytes(), b.tobytes())))
out.save("xor.png")  # open xor.png to read the flag
#crypto{X0Rly_n0t!}
```

## Flag

```text
crypto{X0Rly_n0t!}
```
