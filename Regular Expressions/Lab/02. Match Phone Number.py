import re

telephone = input()
regex = r"([+][359]{3}([ |-])[2]\2[0-9]{3}\2[0-9]{4})\b"

matches = re.findall(regex, telephone)
output = ", ".join([match[0] for match in matches])

print(output)
