def all_the_longest(words: list):
    longest_lst = []
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    longest_lst.append(longest)
    for word in words:
        if len(word) == len(longest) and word != longest:
            longest_lst.append(word)
    return longest_lst
