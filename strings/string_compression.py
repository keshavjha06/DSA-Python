def compress(s):
    s = s.replace(" ", "")
    result = []
    count = 1
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            result.append(s[i])
            result.append(str(count))  # a3b2z2t1k2a2
            count = 1
    return "".join(result)


def compress_while_loop(s):
    s = s.replace(" ", "")
    result = []
    i = 0
    while i < len(s):
        counter = 1
        while i < len(s) - 1 and s[i] == s[i + 1]:
            counter += 1
            i += 1
        result.append(s[i])
        result.append(str(counter))
        i += 1
    return "".join(result)


s = "aaa bb zz t kk aa"
print(compress(s))
print(compress_while_loop(s))
