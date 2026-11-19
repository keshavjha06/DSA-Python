def is_palindrome(word):
    if word is None:
        raise ValueError("Input string cannot be null")
    if word == "":
        return True

    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True


print(is_palindrome("madam"))
