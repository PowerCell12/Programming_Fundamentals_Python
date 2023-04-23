import re

dates = input()
regex = r"([0-9]{2}([-|.|/])[A-Z][a-z]{2}\2[0-9]{4})"
final = re.findall(regex, dates)

for date in final:
    final = date[0]
    if "/" in final:
        final1 = final.split("/")
    elif "." in final:
        final1 = final.split(".")
    elif "-" in final:
        final1 = final.split("-")
    

    print(f"Day: {final1[0]}, Month: {final1[1]}, Year: {final1[2]}")
