def line(n, char):
   print("*" * n) if char == "" else print(char[0] * n)

def square(size, character):
    for _ in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")