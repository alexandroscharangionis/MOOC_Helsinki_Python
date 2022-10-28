list = [1, 2, 3, 4, 5]

while True:
    indx = int(input("Index: "))
    if indx == -1:
        break
    val = int(input("New value: "))
    list[indx] = val
    print(list)
