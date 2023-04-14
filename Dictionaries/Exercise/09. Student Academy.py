PairOfRows = int(input())
Students_Grades  = {}
HowMany = {}

for i in range(PairOfRows):
    name = input()
    grade = float(input())



    if name not in HowMany:
        HowMany[name] = 1
    else:
        HowMany[name] += 1


    if name not in Students_Grades.keys():
        Students_Grades[name] = grade
    else:
        Students_Grades[name] = Students_Grades[name] + grade
        Students_Grades[name] = Students_Grades[name] / HowMany[name]

remove_keys = []
for key in Students_Grades.keys():
    if Students_Grades[key] < 4.50:
        remove_keys.append(key)

for key in remove_keys:
    Students_Grades.pop(key)

    
for key, value in Students_Grades.items():
    print(f"{key} -> {value:.2f}")
