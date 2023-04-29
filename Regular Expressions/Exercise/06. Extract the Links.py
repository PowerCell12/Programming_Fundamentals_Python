import re

list1 = []

while True:
  links = input()

  if links == "":
    break

  regex = r"[www]{3}\.[A-Za-z-0-9]+\.[a-z\.]+"
  final = re.findall(regex, links)

  for i  in range(len(final)):
    matches = final[i]
    if i == len(final) - 1:
      print(matches)
    else:
      print(matches, end="\n")
