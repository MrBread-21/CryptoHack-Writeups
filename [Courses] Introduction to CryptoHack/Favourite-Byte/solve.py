#!/usr/bin/env python3

cipher = bytes.fromhex(
    "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
)

for key in range(256):
    plaintext = bytes(c ^ key for c in cipher)

    if plaintext.startswith(b"crypto{"):
        print(f"Key: {key:#02x}")
        print(plaintext.decode())
        break