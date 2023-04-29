import re
names = input().split(", ")
name = ""
dicts = {}
distance = 0

while True:
    names_and_distance = input()

    if names_and_distance == "end of race":
        break

    regex2 = r"[0-9]+"
    final2 = re.findall(regex2, names_and_distance)
    for i in range(len(final2)):
        current = final2[i]

        for j in range(len(current)):
            current1 = current[j] 
            distance += int(current1)

    regex1 = r"[a-zA-Z]+"
    final1 = re.findall(regex1, names_and_distance)


    for matches in final1:
        name += matches
    

    if name in names and name not in dicts:
        dicts[name] = distance
    elif name in names and name in dicts:
        dicts[name] += distance



    name = ""
    distance = 0


sorted_dict = dict(sorted(dicts.items(), key=lambda item: item[1], reverse=True))

counter = 1

for key in sorted_dict.keys():


    if counter == 1:
        print(f"1st place: {key}")
    elif counter == 2:
        print(f"2nd place: {key}")
    elif counter == 3:
        print(f"3rd place: {key}")

    counter += 1

    if counter == 4:
        break   
