lines = int(input())
index1 = 0
index2 = 0
index3 = 0
index4 = 0


for i in range(lines):
  strings = input()
  
  for j in range(len(strings)):
    if strings[j] == "@":
      index1 = j + 1

    if strings[j] == "|":
      index2 = j

    if strings[j] == "#":
      index3 = j + 1

    if strings[j] == "*":
      index4 =  j


  name = strings[index1:index2]
  age = strings[index3:index4]

  print(f"{name} is {age} years old.")
