name = input()
list = []

for i in range(0, len(name)):
    if name[i].isupper():
        list.append(i)

print(list)
