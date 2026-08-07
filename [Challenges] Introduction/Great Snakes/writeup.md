# Great Snakes

![Great Snakes](challenge.jpg)

## Description

The challenge provides a Python script named `great_snakes.py`. Running the script prints the flag.

## Analysis

The script contains a list of integers:

```python
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
```

The final line of the script is:

```python
print("".join(chr(o ^ 0x32) for o in ords))
```

Each integer is XORed with the hexadecimal value `0x32` before being converted into its ASCII character using `chr()`. The resulting characters are concatenated to form the flag.

Since the script already performs the decoding, the simplest solution is to execute it.

## Solution

Run the script:

```bash
python3 great_snakes.py
```

Output:

```text
Here is your flag:
crypto{z3n_0f_pyth0n}
```

## Flag

```text
crypto{z3n_0f_pyth0n}
```

## Takeaways

- `chr()` converts an integer into its corresponding ASCII character.
- The XOR (`^`) operator is commonly used in cryptography to encode and decode data.
- Python comprehensions provide a concise way to transform sequences.