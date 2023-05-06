integers = list(map(int, input().split()))
counter = 0
list1 = []
list2 =[]


while True:
    indice = input()

    if indice == "End":
        break

    indice = int(indice)

    if indice >= len(integers):
        continue


    number = integers[indice]
    integers[indice] = -1
    counter += 1


    item_to_find = -1
    for idx, value in enumerate(integers):
        if value == item_to_find:
            list1.append(idx)


    for i in range(0, len(integers)):
        current = integers[i]
        if integers.index(current) in list1 and counter > 0:
            pass
        else:
            integers[indice] = number
            if current > integers[indice]:
                integers[i] = current - number
            else:
                integers[i] = current + number
            integers[indice] = -1
    list1 = []


for i in range(0, len(integers)):
    current1 = str(integers[i])
    list2.append(current1)

final = " ".join(list2)

print(f"Shot targets: {counter} -> {final}")
