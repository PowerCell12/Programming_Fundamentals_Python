string = str(input())
string = string.upper()

water = "WATER"
sand = "SAND"
fish = "FISH"
sun = "SUN"
counter = 0

for i in range(0, len(string)):
    if water in string:
        counter += 1
        string = string.replace(water, '', 1)

    if sand in string:
        counter += 1
        string = string.replace(sand, '', 1)

    if fish in string:
        counter += 1
        string = string.replace(fish, '', 1)


    if sun in string:
        counter += 1
        string  = string.replace(sun, '', 1)

print(counter)
