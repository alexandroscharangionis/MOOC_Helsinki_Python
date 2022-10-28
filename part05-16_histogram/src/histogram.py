def histogram(string: str):
    letters = {}
    for letter in string:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    for letter in letters:
        print(letter + " " + "*" * letters[letter])
