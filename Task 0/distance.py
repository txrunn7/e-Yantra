# cook your dish here
import math
def compute_distance(x1, y1, x2, y2):
    diff_x, diff_y = x2-x1, y2-y1
    distance = math.sqrt(pow(diff_x, 2) + pow(diff_y, 2))
    print("Distance:",format(float(distance), ".2f"))


# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
    if 1<= test_cases <= 25:
        for t in range(test_cases):
            values = input("")
            x1 = int(values.split(" ")[0])
            y1 = int(values.split(" ")[1])
            x2 = int(values.split(" ")[2])
            y2 = int(values.split(" ")[3])
            sub = 0
            #sub task 1
            if -20<=x1<=20 and -20<=x2<=20 and -20<=y1<=20 and -20<=y2<=20:
                sub = 1
                compute_distance(x1, y1, x2, y2)
            #sub task 2
            if -100<=x1<=100 and -100<=x2<=100 and -100<=y1<=100 and -100<=y2<=100 and sub == 0:
                compute_distance(x1, y1, x2, y2)    
        