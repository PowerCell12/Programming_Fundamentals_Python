number = int(input())
word = str(input())
list1 = []
list2 = []

for i in range(number):
    strings = str(input())
    
    list1.append(strings)

    if word in strings:
      list2.append(strings)

print(list1)
print(list2)
