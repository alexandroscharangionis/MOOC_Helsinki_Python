def length_of_longest(words: list):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return len(longest)
