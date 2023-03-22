People = list(map(int, input().split(" ")))
number = int(input())
index = 0 
list1 = []

for i in range(0, len(People)):
    index += number -1

    while index >= len(People):
        index = index - len(People)


    if len(People) == 1:
        index = 0


    final = People.pop(index)


    list1.append(final)

listfinal = []
for i in range(0, len(list1)):
    current = str(list1[i])
    listfinal.append(current)


final  = ",".join(listfinal)
final = "[" + final + "]"

print(final)
