def get_output(text):
    tokens = text.split()
    number = int(tokens[-1])
    result = []
    for i in range(len(tokens) - 1):
        pair = tokens[i].split(":")
        divisor = int(pair[0])
        word = pair[1]
        if number % divisor == 0:
            result.append(word)

    if len(result) > 0:
        return "".join(result)
    return str(number)


text = "3:fizz 5:buzz 1"
print(get_output(text))
print(get_output("3:fizz 7:buzz 9:whizz 315"))
