def everything_reversed(strngs: list):
    reversed = []
    for i in range(len(strngs) - 1, -1, -1):
        rev = strngs[i][::-1]
        reversed.append(rev)
    return reversed
