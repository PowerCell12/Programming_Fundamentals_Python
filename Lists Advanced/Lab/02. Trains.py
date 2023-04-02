wagons = int(input())

list = []
list1 = []
list2 = []
add_sum = 0
index_train = 0


for i in range(1, wagons + 1):
    list.append(0)

while True:
    command = input()

    if command == "End":
        break
    
    list1 = command.split()

    if "add" in list1:
        add_sum += int(list1[1])
        index_train = -1 
        list[index_train] += add_sum
        add_sum = 0

    if "insert" in list1:
        index_train = list1[1]
        index_train = int(index_train)
        blah = int(list1[2])
        list[index_train] += blah


    if "leave" in list1:
        index_train = list1[1]
        index_train = int(index_train)
        blah = int(list1[2])
        list[index_train] -= blah

print(list)
