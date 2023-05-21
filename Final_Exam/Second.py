lines = int(input())

import re

for i in range(lines):

    bosses = input()
    final = ""

    pattern = r'\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#'


    final = re.findall(pattern, bosses)


    if len(final) == 0:
        print("Access denied!")
    else:
        print(f"{final[0][0]}, The {final[0][1]}")
        print(f">> Strength: {len(final[0][0])}")
        print(f">> Armor: {len(final[0][1])}")
