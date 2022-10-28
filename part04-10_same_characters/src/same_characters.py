import sre_compile


def same_chars(str, n, m):
    if n >= len(str) or m >= len(str) or str[n] != str[m]:
        return False
    else:
        return True

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))