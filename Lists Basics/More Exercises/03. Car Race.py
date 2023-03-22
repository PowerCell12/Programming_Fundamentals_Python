race = input()
listrace = race.split()
middleIndex = int((len(listrace) - 1)/2)

list2 = []
number1 = 0
number2 = 0

for i in range(0, len(listrace)):
    current_number = int(listrace[i])
    list2.append(current_number)


for i in range(0, len(list2)):
    current_number = int(list2[i])
    if i == middleIndex:
        break
    if list2[i] == 0:
        number1 = number1 * 0.8
        number1 = round(number1, 1)
    else:
        number1 += current_number


for i in range(len(list2) -1, 0, -1):
    current_number = int(list2[i])
    if i == middleIndex:
        break
    if list2[i] == 0:
        number2  = number2 * 0.8
        number2 = round(number2, 1)
    else:
        number2 += current_number

if number1 < number2:
    print(f"The winner is left with total time: {number1:.1f}")
else:
    print(f"The winner is right with total time: {number2:.1f}")
