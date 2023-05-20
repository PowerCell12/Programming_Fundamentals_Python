import re 

string = input()
regex1 = r"(::[A-Z][a-z]{2,}::)|(\*\*[A-Z][a-z]{2,}\*\*)"
final1 = re.findall(regex1, string)

cool_ones = []
for chrs in final1:
    for chrss in chrs:
        if chrss == "":
            pass
        else:
            cool_ones.append(chrss)


cool_threshold = 1

for strs in string:
    if strs.isdigit():
            cool_threshold *= int(strs)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(cool_ones)} emojis found in the text. The cool ones are:")
for final in cool_ones:
    ascci = 0
    for final2 in final:
        if final2 != ":" and final2 != "*":
            ascci += ord(final2)

    if ascci > cool_threshold:
        print(final)
