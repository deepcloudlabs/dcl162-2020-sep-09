x = 123456789101112

numbers = [4, 8, 15, 16, 23, 42]

with open("test.txt", mode="wt") as f:
    for number in numbers:
        f.write(str(number))

f = open("test.data", mode="wb")
f.write(x.to_bytes(6, byteorder="big"))
f.close()

f = open("test.data", mode="rb")
x = int.from_bytes(f.read(), byteorder="big")
print(x)
f.seek(4*500000)
f.close()
