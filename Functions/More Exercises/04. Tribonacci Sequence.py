lines = int(input())
list = []
list.append(1)
list.append(1)
count = 0
list2 = []

if lines == 0:
    print(0)
    quit()

if lines == 1:
    print(1)
    quit()


for i in range(3, lines + 1):
   count += 1
   if count == 1:
    final  = list[-1] + list[-2]
   else:
    final = list[-1] + list[-2] + list[-3]
   list.append(final)

for i in range(0, len(list)):
    current_number = str(list[i])
    list2.append(current_number)

list2 = " ".join(list2)

print(list2)
