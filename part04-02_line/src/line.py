# Write your solution here
def line(n, char):
   print("*" * n) if char == "" else print(char[0] * n)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "XXX")