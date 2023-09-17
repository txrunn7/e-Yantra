def reverse(a):
    b=a[::-1]
    return b
    
def intlist(lst):
    for i in lst:
        if not isinstance(i, int):
            return False
    return True
    
def conrange(lst):
    for i in lst:
        if -100<=i<=100:
            return False
    return True



    
test_cases=int(input())

if 1<=test_cases<=25:

 for cases in range(1,test_cases+1):
    N = int(input())
    
    if 8<=N<=50:
     L = list(map(int, input().split()))
     
    
     if conrange(L) and intlist(L):
    
      for i in reverse(L):
        print(i,end=" ")
      print()   
    
      for i in range(0, N, 3):
       if i!=0:
        print(L[i]+3,end=" ")
      print()   
    
    
      for i in range(0, N, 5):
       if i!=0:
        print(L[i]-7,end=" ")
      print()
   
      print(sum(L[3:8]))
