arr = ["K", "e", "s", "h", "a", "v"]
for ele in arr:
    print(ele, end=" ")
text = "Keshav"
print(text)

s = "Keshav Jha"
print(s.find("s"))
print(s.rfind("a"))           # last index
print(s.find("t"))            # -1 as it's not there
print(s.lower())
print(s.upper())
print(s.strip())              # remove leading and trailing whitespace
print("Kesh" in s)            # True
print(s.startswith("Kesh"))   # True
print(s.endswith("Kesh"))     # False
print(len(s) == 0)            # False (isEmpty)
print(len(s))                 # 10
print(s.replace("Keshav", "Utkarsh"))     # Utkarsh Jha
print(s.replace("Utkarsh", "Keshav", 1))  # Keshav Jha (replace first only)
print(s.replace("Keshav", "Utkarsh"))     # Utkarsh Jha
print(s[0:3])
print(s[3:])
