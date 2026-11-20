# a list of characters is Python's closest thing to a StringBuilder
s = "Keshav"
sb = list(s)
i = 0
j = len(sb) - 1
while i <= j:
    sb[i], sb[j] = sb[j], sb[i]
    i += 1
    j -= 1
print("".join(sb))  # vahseK
del sb[1]
print("".join(sb))  # vhseK
sb.insert(1, "a")
print("".join(sb))  # vahseK

# quick reverse with slicing
text = "Aditya"
text = text[::-1]
print(text)  # aytidA
