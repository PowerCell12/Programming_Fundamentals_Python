import re
text = input()

regex1 = r"(#[a-zA-Z]{3,}##[a-zA-Z]{3,}#)|(@[a-zA-Z]{3,}@@[a-zA-Z]{3,}@)"
final1 = re.findall(regex1, text)
valid_pairs = []
mirror_list = []

for chrss in final1:
    for chrs in chrss:
        if chrs == "":
            pass
        else:
            valid_pairs.append(chrs)


if len(valid_pairs) == 0:
    print("No word pairs found!")
else:
    print(f"{len(valid_pairs)} word pairs found!")

for matches in valid_pairs:
    matches_final = []
    if "#" in matches:
        matches_final = matches.split("#")
        while "" in matches_final:
            matches_final.remove("")
    elif "@" in matches:
        matches_final = matches.split("@")
        while "" in matches_final:
            matches_final.remove("")


    if matches_final[0] == matches_final[1][::-1]:
        mirror_list.append(matches_final[0])
        mirror_list.append(matches_final[1])


if len(mirror_list) == 0:
    print("No mirror words!")
    quit()

print("The mirror words are:")
for value1 in range(1, len(mirror_list), 2):
    current = mirror_list[value1]

    current1 = mirror_list[value1 - 1]

    if value1 != len(mirror_list) -1:
        print(f"{current1} <=> {current}", end=", ")
    else:
        print(f"{current1} <=> {current}")
