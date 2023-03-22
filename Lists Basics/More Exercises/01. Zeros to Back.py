string = input()
list  = string.split(", ")
list1 = []


for i in range(0, len(list)):
    current_number = int(list[i])
    if current_number == 0:
        list += [list.pop(i)]

for i in range(0, len(list)):
    current_number = int(list[i])
    if current_number == 0:
        list += [list.pop(i)]

for i in range(0, len(list)):
    current_number = int(list[i])
    if current_number == 0:
        list += [list.pop(i)]


for i in range(0, len(list)):
    current_number = int(list[i])
    list1.append(current_number)


print(list1)
