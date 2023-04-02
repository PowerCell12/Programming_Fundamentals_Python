text = input()

length = len(text)
list = ["a", "o", "u", "e", "i"]

list1 = []

for i in range(0, length):
    current = text[i]
    list1.append(current)


for i in range(0, length):
    current = text[i]
    if current.lower() in list:
        list1.remove(current)

list2 = "".join(list1)

print(list2)
