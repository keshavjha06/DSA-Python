s = "abc"  # strings are immutable
s2 = "abc"
s1 = "abc" + "d"

# Python has no StringBuilder/StringBuffer; use a list of pieces and "".join
sb = list("abc")
sb.append("a")     # abca
sb.insert(1, "b")  # abbca
sb.reverse()       # acbba
s4 = "".join(sb)

print(s == s2)   # == compares values
print(s1 == "abcd")

length = len(s1)  # 4
for i in range(length):
    print(s1[i])

chars = list(s1)  # like toCharArray()
str3 = "".join(chars)
for ch in chars:
    print(ch)

b = "I am practicing GFG"
print(b.split())                  # ['I', 'am', 'practicing', 'GFG']
print(b.replace(" ", ""))         # IampracticingGFG
print(b.replace("pract", ""))     # I am icing GFG
print(b.replace(" ", "", 1))      # Iam practicing GFG
words = "I am practicing".split(" ")
print("-".join(words))            # I-am-practicing

e = s[0]       # a
f = chr(65)    # A
print(e, f, ord("a"))  # ASCII: A-Z -> 65-90, a-z -> 97-122

print("a".isalpha())  # True
print("1".isdigit())  # True
print("b".isupper())  # False

g = "123"
a = int(g)   # 123
h = 12
text = str(h)  # "12"
print(a, text)
