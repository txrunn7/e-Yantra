def run():
    for i in range(T):
        string = input("")
        start = 0
        net_list = string.split(" ")
        length = len(net_list)
        for i in range(length):
            each_element = net_list[i]
            if each_element[0] == "@":
                start = 1
            if start == 1 and i != length-1:
                if each_element[0] != "@":
                    print(len(each_element), end=",")
                else:
                    print(len(each_element)-1, end=",")
            if start == 1 and i == length-1:
                print(len(each_element))

T = int(input(""))
t_val = 0
#subtask 1
if T <= 5:
    t_val = 1
    run()
#subtask 2
if 1 <= T <= 25 and t_val == 0:
    run()
