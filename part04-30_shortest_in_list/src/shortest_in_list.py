def shortest(words: list):
    short = words[0]
    for word in words:
        if len(word) < len(short):
            short = word
    return short
