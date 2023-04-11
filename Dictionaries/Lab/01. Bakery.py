food = input()

food1 = food.split(" ")
bakery = {}

for i in range(0, len(food1), 2):
    key = food1[i]
    value = int(food1[i + 1])
    bakery[key] = value


print(bakery)
