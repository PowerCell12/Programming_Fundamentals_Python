factor = int(input())
count = int(input())
list = []
number = 0

for i in range(1,count + 1):
    count = int(count)
    number += 1 
    counts = factor * number
    list.append(counts)

print(list)
