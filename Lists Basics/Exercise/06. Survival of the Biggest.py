integers = input()
toremove = int(input())
list = integers.split()
list1 = []
list2 = []


for i in range(0, len(list)):
    current_number = int(list[i])
    list1.append(current_number)

for i in range(toremove):
    list1.remove(min(list1))

for i in range(0, len(list1)):
    current_number = str(list1[i])
    list2.append(current_number)

list3 = ", ".join(list2)

print(list3)
