import re 
list1 = []

while True:
  lines = input()

  if  lines == "":
    break
  
  final = "[0-9]+"
  matches = re.findall(final, lines)
  
  for match in matches:
    list1.append(match)

print(" ".join(list1))
