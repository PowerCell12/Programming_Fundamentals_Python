text = input()
import re

final = r'(#[a-zA-Z ]+#[0-9]{2}\/[0-9]{2}\/[0-9]{2}#([\d|[1-9]\d{1,3}|10000]{1}])#)|(\|[a-zA-Z ]+\|[0-9]{2}\/[0-9]{2}\/[0-9]{2}\|([\d|[1-9]\d{1,3}|10000]{1}])\|)'
final1= re.findall(final, text)
calories = 0

true = []

for thing in final1:

    for things in thing:
        if things != "":
            if things[0] == "#" or things[0] == "|":
                true.append(things)


calories  = 0

for things3 in true:

    if things3[0] == "#":
        current = things3.split("#")
    else:
        current = things3.split("|")

    calories += int(current[3])

days  = int(calories / 2000)

print(f"You have food to last you for: {days} days!")

for things4 in true:

    if things4[0] == "#":
        current = things4.split("#")
    else:
        current = things4.split("|")

    print(f"Item: {current[1]}, Best before: {current[2]}, Nutrition: {current[3]}")
