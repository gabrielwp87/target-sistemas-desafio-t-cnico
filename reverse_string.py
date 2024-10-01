def reverse_string(word):
    result = ""
    size = len(word)
    for i in range(size):
        result += word[size - (i + 1)]

    print(result)

word_to_invert = input("Informe a palavra que deseja inverter: ")
reverse_string(word_to_invert)


