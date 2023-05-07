# binary pack

import struct

var1, var2, var3 = "a", "b", "c"

data = struct.pack("10s 10s 10s", var1.encode(), var2.encode(), var3.encode())

var1, var2, var3 = struct.unpack("10s 10s 10s", data)
# need decode strings, and remove blank bytes at end of string
print("var1: ", var1.decode().rstrip("\x00)"))
print("-------------------------------")
# -------------------------------

var1, var2, var3 = 1, 1.3, b"abc"

data = struct.pack("i f 10s", var1, var2, var3)

var1, var2, var3 = struct.unpack("i f 10s", data)
# need decode strings, and remove blank bytes at end of string
# unsolved error in float numbers transfer
print("var1: ", var1)
print("var2: ", var2)
print("var3: ", var3)
print("var3: ", var3.decode().rstrip("\x00)"), " (decoded)")
# -------------------------------
