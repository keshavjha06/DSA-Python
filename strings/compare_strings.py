# Works like Java's a.compareTo(b)
def compare_to(a, b):
    i = 0
    j = 0
    len1 = len(a)
    len2 = len(b)
    while i < len1 and j < len2:
        if a[i] != b[j]:
            return ord(a[i]) - ord(b[j])
        i += 1
        j += 1
    return len1 - len2


a = "raghav"  # harmeet
b = "preet"   # harsh   m - s -> -6
print(compare_to(a, b))  # r - p i.e 2
