def line(n, char):
    print("*" * n) if char == "" else print(char[0] * n)


def box_of_hashes(height):
    for _ in range(height):
        line(10, "#")
