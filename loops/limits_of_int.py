import sys

# Java's int is 32-bit; Python ints are unbounded and never overflow.
INT_MAX = 2**31 - 1
INT_MIN = -(2**31)

print(INT_MAX)
print(INT_MIN)
print(INT_MAX + 10)  # needs a long in Java, just works in Python
print(sys.maxsize)  # largest native index size, not a limit on int
