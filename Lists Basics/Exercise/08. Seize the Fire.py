firesWithTheirCelss = input().split("#")
waterHave = int(input())
list1 = []
effor = 0
totalFire = 0


for i in range(0, len(firesWithTheirCelss)):
    currentCell = firesWithTheirCelss[i]
    currentCell1 = currentCell

    currentCell = currentCell.split(" = ")

    if currentCell[0] == "High":
        if int(currentCell[1]) < 81 or int(currentCell[1]) > 125:
            continue
    elif currentCell[0] == "Medium":
        if int(currentCell[1]) < 51 or int(currentCell[1]) > 80:
            continue
    elif currentCell[0] == "Low":
        if int(currentCell[1]) < 1 or int(currentCell[1]) > 50:
            continue

    if waterHave - int(currentCell[1]) < 0:
        continue

    waterHave = waterHave - int(currentCell[1])
    list1.append(currentCell[1])

    effor += int(currentCell[1]) * 0.25

    totalFire += int(currentCell[1])

print("Cells:")
for item in list1:
    print("- "  + str(item))

print(f"Effort: {effor:.2f}")
print(f"Total Fire: {totalFire}")
