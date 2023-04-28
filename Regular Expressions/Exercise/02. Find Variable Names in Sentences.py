import re

strings = input()

regux = r"\b[_]{1}[A-Za-z]+\b"
final = re.findall(regux, strings)

for i in range(len(final)):
  match = final[i]
  match = match[1:]

  if i < len(final) - 1:
    print(match, end=",")
  else:
    print(match)
