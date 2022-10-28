list = []
count = 0
while True:
    print(f"The list is now {list}")
    inpt = input("a(d)d, (r)emove or e(x)it: ")
    match inpt:
        case "d":
            list.append(count + 1)
            count += 1
        case "r":
            list.pop(-1)
            count -= 1
        case "x":
            print("Bye!")
            break
