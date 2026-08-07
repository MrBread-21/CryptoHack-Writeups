# ASCII

![ASCII](challenge.jpg)

## Description

The challenge provides an array of integers and explains that ASCII is a 7-bit character encoding standard.

The objective is to convert each integer into its corresponding ASCII character to recover the flag.

## Analysis

The given array is:

```python
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
```

In Python, the `chr()` function converts an integer into its corresponding ASCII character. By applying `chr()` to every element in the list and concatenating the results, we obtain the original string.

## Solution

```python
ords = [
    99, 114, 121, 112, 116, 111, 123,
    65, 83, 67, 73, 73, 95, 112,
    114, 49, 110, 116, 52, 98,
    108, 51, 125
]

flag = "".join(chr(c) for c in ords)
print(flag)
```

Output:

```text
crypto{ASCII_pr1nt4bl3}
```

## Flag

```text
crypto{ASCII_pr1nt4bl3}
```

## Takeaways

- ASCII maps integers (0–127) to printable characters and control characters.
- `chr()` converts an integer to a character, while `ord()` performs the reverse conversion.
- Converting lists of ASCII values into strings is a common introductory task in cryptography and CTF challenges.