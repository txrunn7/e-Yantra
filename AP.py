from functools import reduce


def generate_AP(a1, d, n):

    AP_series = []

    for i in range(0, n):
        AP_series.append(a1 + (i * d))

    return AP_series


test_cases = int(input())

if 1 <= test_cases <= 25:

    for case in range(1, test_cases + 1):
        inp = input()
        values = inp.split()

        a = int(values[0])
        d = int(values[1])
        n = int(values[2])

        if 1 <= a <= 100 and 1 <= d <= 100 and 1 <= n <= 100:
            ap = generate_AP(a, d, n)

            for i in ap:
                print(i, end=" ")
            print()

            squared_numbers = list(map(lambda x: x**2, ap))

            for i in squared_numbers:
                print(i, end=" ")
            print()

            sum = reduce(lambda x, y: x + y, squared_numbers)
            print(sum)

else:
        
        if 1<=a<=20 and 1<=d<=20 and 1<=n<=20:
            ap=generate_AP(a,d,n)

        for i in ap:
            print(i, end=" ")


            squared_numbers = list(map(lambda x: x ** 2, ap))
        
            for i in squared_numbers:
             print(i,end=" ")
            print('\n')

            sum= reduce(lambda x, y: x + y, squared_numbers)
            print(sum)



            

          
<<<<<<< HEAD
=======
          
>>>>>>> ca15fa2ba8d28aedaba225baad3d93ef73e74bd7
