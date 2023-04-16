name1 = input().split(" ")
final_sum = 0
toBeTo = None
moreThan = None
current = name1[0]
current1 = name1[1]

if len(name1[0]) > len(name1[1]):
    moreThan = current[len(name1[1]):]
    toBeTo = name1[1]

    for something in moreThan:
        final_sum += ord(something)
elif len(name1[0]) < len(name1[1]):
    moreThan = current1[len(name1[0]):]
    toBeTo = name1[0]

    for something in moreThan:
        final_sum += ord(something)
else:
    toBeTo = name1[0]

for i in range(0, len(toBeTo)):

    final1 = ord(current[i])
    final2 = ord(current1[i])

    final_sum += final1 * final2

print(final_sum)
