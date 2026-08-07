# Hex

![Hex](challenge.jpg)

## Description

The challenge provides a hexadecimal-encoded string and asks us to decode it back into its original bytes to recover the flag.

## Analysis

Hexadecimal is a base-16 representation where each byte is represented by two hexadecimal digits.

Python provides the `bytes.fromhex()` function to convert a hexadecimal string into bytes. The resulting bytes can then be decoded into a UTF-8 string to reveal the flag.

## Solution

```python
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

flag = bytes.fromhex(hex_string).decode()

print(flag)
```

Output:

```text
crypto{You_will_be_working_with_hex_strings_a_lot}
```

## Flag

```text
crypto{You_will_be_working_with_hex_strings_a_lot}
```

## Takeaways

- Hexadecimal represents one byte using two hexadecimal digits.
- `bytes.fromhex()` converts a hexadecimal string into raw bytes.
- `.decode()` converts bytes into a human-readable string using UTF-8.