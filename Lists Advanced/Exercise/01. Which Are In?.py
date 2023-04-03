first = input().split(", ")
second =  input().split(", ")
list2 = []

for i in range(0, len(first)):
    for y in range(0, len(second)):
        if first[i] in second[y]:
            if first[i] in list2:
                continue
            else:
                list2.append(first[i])

print(list2)
