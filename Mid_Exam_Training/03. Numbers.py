numbers = list(map(int, input().split()))
how_many = 0
length = len(numbers)
list  = []
list1 = []

for i in range(0, (len(numbers))):
    how_many += numbers[i]

average = how_many / length


for i in range(0, len(numbers)):
    current = numbers[i]
    if current > average:
     list.append(current)

if not list:
    print("No")
else:
    list.sort(reverse=True)

    for i in range(0, len(list)):
        if len(list) > 5:
            list.pop()


    for i in range(0, len(list)):
        current = str(list[i])
        list1.append(current)

    list_final = " ".join(list1)
    print(list_final)
