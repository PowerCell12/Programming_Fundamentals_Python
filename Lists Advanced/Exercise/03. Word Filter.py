text = input().split()
list2 = []

for i in range(0, len(text)):
    if len(text[i]) % 2 == 0:
        list2.append(text[i])
        

list3  = "\n".join(list2)
print(list3)
