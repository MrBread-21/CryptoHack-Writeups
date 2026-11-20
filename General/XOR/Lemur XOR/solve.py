from PIL import Image

a = Image.open("lemur.png").convert("RGB")
b = Image.open("flag.png").convert("RGB")
out = Image.frombytes("RGB", a.size, bytes(x ^ y for x, y in zip(a.tobytes(), b.tobytes())))
out.save("xor.png")  # open xor.png to read the flag
#crypto{X0Rly_n0t!}
