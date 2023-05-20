dict_cities = {}


## first population and then gold
while True:
    commands = input().split("||")

    if commands[0] == "Sail":
        break

    if commands[0] not in dict_cities:
        dict_cities[commands[0]] = []
        dict_cities[commands[0]].append(int(commands[1]))
        dict_cities[commands[0]].append(int(commands[2]))
    else:
        dict_cities[commands[0]][0] += int(commands[1])
        dict_cities[commands[0]][1] += int(commands[2])


while True:
    commands1 = input().split("=>")

    if commands1[0] == "End":
        break

    if commands1[0] == "Plunder":
        dict_cities[commands1[1]][0] -= int(commands1[2])
        dict_cities[commands1[1]][1] -= int(commands1[3])

        print(f"{commands1[1]} plundered! {commands1[3]} gold stolen, {commands1[2]} citizens killed.")

        if dict_cities[commands1[1]][0] <= 0 or dict_cities[commands1[1]][1] <= 0:
            del dict_cities[commands1[1]]
            print(f"{commands1[1]} has been wiped off the map!")


    if commands1[0] == "Prosper":
        ## if error do equal to 0 too 
        if int(commands1[2]) < 0:
            print("Gold added cannot be a negative number!")
            continue

        dict_cities[commands1[1]][1] += int(commands1[2])
        print(f"{commands1[2]} gold added to the city treasury. {commands1[1]} now has {dict_cities[commands1[1]][1]} gold.")

if dict_cities:
    print(f"Ahoy, Captain! There are {len(dict_cities)} wealthy settlements to go to:")
    for key,value in dict_cities.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
