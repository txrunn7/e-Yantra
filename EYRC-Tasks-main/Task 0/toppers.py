T = int(input(""))
if 1 <= T <= 25: 
    for tests in range(T):
        N = int(input(""))
        if 2 <= N <= 100:
            mark_list = {}
            students = []
            highest_mark = 0
            for numbers in range(N):
                name_and_marks = input("")
                name_and_marks = name_and_marks.split(" ")
                if 0 <= float(name_and_marks[1]) <= 100: 
                    mark_list[name_and_marks[0]] = float(name_and_marks[1])
            if len(mark_list) != 0:
                for marks in mark_list.keys():
                    if highest_mark < mark_list[marks]:
                        students.clear()
                        highest_mark = mark_list[marks]
                        students.append(marks)
                    elif highest_mark == mark_list[marks] and mark_list[marks] not in students:
                        students.append(marks)
                for student in sorted(students):
                    print(student)


            

