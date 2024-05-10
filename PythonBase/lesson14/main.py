'''for i in (0, 1, 2, 3, 4, 5, 62, 63, 64, 65, 126, 127, 128, 129, 254, 255):
    print(f"{i} = {i:08b}")
    print(bin(i))

print(bin(-10), f"{-10:08b}")

import struct

for i in (4, 3, 2, 1, 0, -1, -2, -3, -4):
    byte = struct.pack("b", i)[0]
    print(f"{i} = {byte:08b}")
'''

num_chars = tuple()
bin_chars = tuple()

for char in "PYTHON":
    print(f"{char} = {ord(char)} = {bin(ord(char))}")

    num_chars += tuple((ord(char),))

for i in num_chars:
    print(f"{i} = {chr(i)}")



