import sys

# Zad 1

a = b = c = "Python 2023"
sys.getrefcount(a) # 4

print(a == b) # True
print(b == c) # True
print(type(a), type(b), type(c)) # <class 'str'> <class 'str'> <class 'str'>
print(hex(id(a)), hex(id(b)), hex(id(c))) # 0x1e637e7e5b0 0x1e637e7e5b0 0x1e637e7e5b0

print("\n-------------------\n")

c = "Java 11"
print(a == b) # True
print(b == c) # False
print(type(a), type(b), type(c)) # <class 'str'> <class 'str'> <class 'str'>
print(hex(id(a)), hex(id(b)), hex(id(c))) # 0x1e637e7e5b0 0x1e637e7e5b0 0x1e637e7e4f0