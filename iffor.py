def procedure(test_cases, sub):
    for tests in range(test_cases):
            n = int(input())
            if sub == 1 and n<=30:
                for i in range(n):
                    if i != 0:
                        if i % 2 != 0:
                            print(i**2, end=" ")
                        else:
                            print(2*i, end=" ")
                    else:
                        print(i + 3, end=" ")
                print()
            if sub == 2 and 0 <= n <= 100:
                for i in range(n):
                    if i != 0:
                        if i % 2 != 0:
                            print(i**2, end=" ")
                        else:
                            print(2*i, end=" ")
                    else:
                        print(i + 3, end=" ")
                print()
# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
    t_val = 0
    #subtask 1
    if test_cases <= 10:
        t_val = 1
        procedure(test_cases, 1)
    #subtask 2
    if 1 <= test_cases <= 25:
        if t_val == 0:
            procedure(test_cases, 2)

    # Write your code from here
    