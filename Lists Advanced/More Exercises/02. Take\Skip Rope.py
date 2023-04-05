string = input()
list1 = []
list2 = []
list3 = []

for i in string:
    if i.isdigit():
      list1.append(i)
    else:
      list3.append(i)

list2 = list(map(int, list1))
take = []
skip = []
taken = ""

for i in range(0, len(list2)):
  if i % 2 == 0:
    take.append(list2[i])
  else:
    skip.append(list2[i])

for i in range(0, len(take)):
  to_take = take[i]
  to_skip = skip[i]

  for j in range(0, to_take):
    if not list3:
      continue
    taken += list3[0]
    list3.pop(0)

  for p in range(0, to_skip):
    if not list3:
      continue
    list3.pop(0)


print(taken)
