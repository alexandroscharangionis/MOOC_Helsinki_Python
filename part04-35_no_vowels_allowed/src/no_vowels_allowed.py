def no_vowels(word):
    devoweled = ""
    for char in word:
        match char:
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                devoweled += char
    return devoweled
