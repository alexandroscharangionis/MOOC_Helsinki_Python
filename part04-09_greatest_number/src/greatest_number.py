def greatest_number(a, b, c):
    return sorted([a, b, c])[-1]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)