def line(n, char):
   print("*" * n) if char == "" else print(char[0] * n)

def shape(n, char, m, char_2):
    for i in range(n):
        line(i + 1, char)

    for j in range(m):
        line(n, char_2)
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")