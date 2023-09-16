def dec_to_binary(n):
    bin_num = None
    
    def dtbr(n, bin_num):
        if bin_num is None:
            bin_num = ""
        
        if n == 0:
            while len(bin_num) < 8:
                bin_num = "0" + bin_num
            return bin_num
        else:
            rem = n % 2
            bin_num = str(rem) + bin_num
            return dtbr(n // 2, bin_num)
    
    bin_num = dtbr(n, None)
    return bin_num

# Main function
if __name__ == '__main__':
    
    test_cases = int(input())
    x = []
    
    if 1<=test_cases<=25:

     for case in range(1, test_cases + 1):
        n = int(input())
        if 0<=n<=255:
         x.append(dec_to_binary(n))
        
        else:
            print("Does not match the given constraint")

     for i in x:
        print(i)
        
    else:
        print("Does not match the given constraint")
