T = int(input())
for i in range(T):
    items = []
    N = int(input())
    for j in range(N):
        item_and_quantity = input()
        item_and_quantity = item_and_quantity.split(" ")
        items.append([item_and_quantity[0], int(item_and_quantity[1])])
    M = int(input())
    for k in range(M):
        operation = input()
        operation = operation.split(" ")
        for val in range(len(items)):
            if operation[1].lower() in items[val]:
                items.remove(items[val])
                net_value = items[val][1] + int(operation[2])
                items.append([operation[1],net_value])
        print("ADDED", operation[1], operation[2])
    print(items)
