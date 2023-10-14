T = int(input())
yes = 0
if 1 <= T <= 25:
    for i in range(T):
        L = []
        net_items = []
        N = int(input())
        if 1 <= N <= 100 and not yes:
            for j in range(N):
                item_and_quantity = input()
                item_and_quantity = item_and_quantity.split(" ")
                if 1 <= int(item_and_quantity[1]) <= 100 and item_and_quantity[0].lower() not in net_items:
                    L.append([item_and_quantity[0].lower(), int(item_and_quantity[1])])
                    net_items.append(item_and_quantity[0].lower())
                else:
                    yes = True
                    break
            if not yes:
                M = int(input())
                if 1 <= M <= 100:
                    for k in range(M):
                        operation = input()
                        operation = operation.split(" ")
                        if operation[0].lower() == "add":
                            if operation[1].lower() in net_items:
                                index = 0
                                for t in L:
                                    if t[0] == operation[1].lower():
                                        index = L.index(t)
                                current_stock = L[index][1]
                                L.pop(index)
                                L.append([operation[1].lower(), current_stock + int(operation[2])])
                                print("UPDATED Item", operation[1])
                                
                            else:
                                L.append([operation[1].lower(), int(operation[2])])
                                print("ADDED Item", operation[1])


                                
                        elif operation[0].lower() == "delete":
                            if operation[1].lower() in net_items:
                                index2 = 0
                                for m in L:
                                    if m[0] == operation[1].lower():
                                        index2 = L.index(m)
                                current_stock = L[index2][1]
                                if current_stock < int(operation[2]):
                                    print(f"Item {operation[1]} could not be DELETED")
                                else:
                                    L.pop(index2)

                                    L.append([operation[1].lower(), current_stock - int(operation[2])])
                                    print(f"DELETED Item {operation[1]}")

                            else:
                                print(f"Item {operation[1]} does not exist")
                    net = 0
                    for totals in L:
                        net += int(totals[1])
                    print(f"Total Items in Inventory: {net}")
            else:
                break
        else:
            break