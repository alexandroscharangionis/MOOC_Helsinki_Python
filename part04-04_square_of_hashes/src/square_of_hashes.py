def line(n, char):
    print("*" * n) if char == "" else print(char[0] * n)


def square_of_hashes(size):
    for _ in range(size):
        line(size, "#")
