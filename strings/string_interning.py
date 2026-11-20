import sys

# == compares values (Java's equals), "is" compares objects (Java's ==)
s1 = "Keshav"
s2 = "".join(["Kes", "hav"])  # builds a new string object, like new String("Keshav")
print(s1 == s2)
print(s1 is s2)

s3 = sys.intern(s2)  # like s2.intern(): returns the shared copy
print(s1 == s3)
print(s1 is s3)
