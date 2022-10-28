def no_shouting(words: list):
    not_capitalized = []
    for word in words:
        if word.isupper():
            continue
        else:
            not_capitalized.append(word)
    return not_capitalized
