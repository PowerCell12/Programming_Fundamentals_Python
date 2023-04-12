dictOfMetals = {}

while True:
    TypeOfMetal = input()

    if TypeOfMetal == "stop":
        break

    HowMuch = int(input())

    if TypeOfMetal not in dictOfMetals:
        dictOfMetals[TypeOfMetal] = HowMuch
    else:
        dictOfMetals[TypeOfMetal] = int(dictOfMetals[TypeOfMetal] + HowMuch)


for key, value in dictOfMetals.items():
    print(f"{key} -> {value}")
