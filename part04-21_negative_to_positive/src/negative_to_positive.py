n = int(input("Please type in a positive integer: "))

for i in range(-n, n + 1):
    if i == 0:
        continue
    print(i)