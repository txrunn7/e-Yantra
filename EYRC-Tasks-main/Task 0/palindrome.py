def pallindrome(string):
    string = string.lower()
    rev_string = ""
    for i in range(len(string)):
        rev_string += string[-1-i]
    if rev_string == string:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

T = int(input(""))
t_val = 0
#subtask 1
if T <= 5:
    t_val = 1
    for i in range(T):
        string = input("")
        if len(string) <= 70:
            pallindrome(string)
        else:
            break

#subtask 2
if 1 <= T <= 25:
    if t_val == 0:
        for i in range(T):
            string = input("")
            if 2 <= len(string) <= 100:
                pallindrome(string)
            else:
                break