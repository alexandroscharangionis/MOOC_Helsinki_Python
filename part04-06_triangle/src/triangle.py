def line(n, char):
   print("*" * n) if char == "" else print(char[0] * n)

def triangle(size):
    for i in range(size):
        line(i + 1, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
