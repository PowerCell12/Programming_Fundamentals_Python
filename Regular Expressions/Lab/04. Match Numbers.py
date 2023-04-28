import re

numbers = input()
redex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(redex, numbers)

for match in matches:
    print(match.group(), end=" ")
