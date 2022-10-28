item_n = int(input("How many items: "))
item_list = []

for i in range(item_n):
    item = int(input(f"Item {i + 1}: "))
    item_list.append(item)

print(item_list)
