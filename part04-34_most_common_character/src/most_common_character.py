def most_common_character(word):
    most_common = ""
    most_occurences = 0
    for char in word:
        occurences = word.count(char)
        if occurences > most_occurences:
            most_common = char
            most_occurences = occurences
    return most_common
