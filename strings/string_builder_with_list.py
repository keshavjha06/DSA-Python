# list of characters used like a StringBuilder (Python lists have no "capacity")
sb = list("Keshav")
print(len(sb))
print("".join(sb))
sb.extend("Jha")  # append
print("".join(sb))
sb[1] = "o"       # setCharAt
print("".join(sb))
t = "".join(sb)   # toString
print(t)
