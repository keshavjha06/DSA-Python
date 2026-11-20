s = "keshav"
s = s + " is a good boy"
s += str(10)  # Python needs str() to join a number to a string
s += "a"
s += "\n"  # moves to next line
s += "n"
print(s)
print("keshav" + str(10) + str(20))  # keshav1020
print(str(10 + 20) + "keshav")       # 30keshav
print(str(10) + "keshav" + str(20))  # 10keshav20
