def spruce(n):
    print("a spruce!")
    count = 1
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" * count)
        count += 2
    print(" " * (n - 1), end="")
    print("*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
