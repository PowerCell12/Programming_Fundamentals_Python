list_tic = []
line1 = input().split(" ")
line2 = input().split(" ")
line3 = input().split(" ")

list_tic.append(line1)
list_tic.append(line2)
list_tic.append(line3)

current = []
current1 = []
current2 = []
current3 = []
current4 = []

counter = 0
counter1 = len(list_tic) - 1
for j in range(len(list_tic)):
  current.append(list_tic[j][0])
  current1.append(list_tic[j][1])
  current2.append(list_tic[j][2])
  current3.append(list_tic[j][counter])
  counter += 1
  current4.append(list_tic[j][counter1])
  counter1 -= 1

counter_final  = 0
## if 000
result = all(elements == line1[0] for elements in line1)
if (result):
  if line1[0] == "1":
    print("First player won")
    quit()
  elif line1[0] == "2":
    print("Second player won")
    quit()
  elif line1[0] == "0":
    counter_final += 1
else:
  counter_final += 1

result1 = all(elements == line2[0] for elements in line2)
if (result1):
  if line2[0] == "1":
    print("First player won")
    quit()
  elif line2[0] == "2":
    print("Second player won")
    quit()
  elif line2[0] == "0":
    counter_final += 1
else:
  counter_final += 1

result2 = all(elements == line3[0] for elements in line3)
if (result2):
  if line3[0] == "1":
    print("First player won")
    quit()
  elif line3[0] == "2":
    print("Second player won")
    quit()
  elif line3[0] == "0":
    counter_final += 1
else:
  counter_final += 1


result3 = all(elements == current[0] for elements in current)
if (result3):
  if current[0] == "1":
    print("First player won")
    quit()
  elif current[0] == "2":
    print("Second player won")
    quit()
  elif current[0] == "0":
    counter_final += 1
else:
  counter_final += 1

result4 = all(elements == current1[0] for elements in current1)
if (result4):
  if current1[0] == "1":
    print("First player won")
    quit()
  elif current1[0] == "2":
    print("Second player won")
    quit()
  elif current1[0] == "0":
    counter_final += 1
else:
  counter_final += 1

result5 = all(elements == current2[0] for elements in current2)
if (result5):
  if current2[0] == "1":
    print("First player won")
    quit()
  elif current2[0] == "2":
    print("Second player won")
    quit()
  elif current2[0] == "0":
    counter_final += 1
else:
  counter_final += 1

result6 = all(elements == current3[0] for elements in current3)
if (result6):
  if current3[0] == "1":
    print("First player won")
    quit()
  elif current3[0] == "2":
    print("Second player won")
    quit()
  elif current3[0] == "0":
    counter_final += 1
else:
  counter_final += 1

result7 = all(elements == current4[0] for elements in current4)
if (result7):
  if current4[0] == "1":
    print("First player won")
    quit()
  elif current4[0] == "2":
    print("Second player won")
    quit()
  elif current4[0] == "0":
    counter_final += 1
else:
  counter_final += 1

print("Draw!")
