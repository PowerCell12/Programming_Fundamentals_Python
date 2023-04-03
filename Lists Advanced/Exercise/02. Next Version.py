version = input().split(".")
list = []
list1 = []
list2 = []

for i in range(0, len(version)):
    current_number1 = int(version[-1])
    current_number2 = int(version[-2])
    current_number3 = int(version[-3])
    current_number1 = current_number1 + 1
    if current_number1 > 9:
        current_number1  = 0
        current_number2 = current_number2 + 1

    if current_number2 > 9:
        current_number2 = 0
        current_number3 = current_number3 + 1


list.append(current_number3)
list.append(current_number2)
list.append(current_number1)

for i in range(0, len(list)):
    current_number1 = str(list[i])
    list1.append(current_number1)



list2 = ".".join(list1)


print(list2)
