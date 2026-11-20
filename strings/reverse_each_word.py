def reverse_words(s):
    # split() with no argument splits on any run of spaces and ignores leading/trailing ones
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)


s = " Archit   is   a good  boy "
print("Original: '" + s + "'")
s = reverse_words(s)
print("Reversed: '" + s + "'")
