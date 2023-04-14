dict_Companies = {}
sameOrNOt = False


while True:
    command = input()

    if command == "End":
        break

    command = command.split(" -> ")

    if command[0] not in dict_Companies:
        dict_Companies[command[0]] = []
    

    for i in range(0, len(dict_Companies[command[0]])):
        current = dict_Companies[command[0]][i]
        if command[1] == current:
            sameOrNOt = True

    if sameOrNOt:
        pass
    else:
        dict_Companies[command[0]].append(command[1])

    sameOrNOt  = False

for key,value in dict_Companies.items():
    print(f"{key}")
    for j in range(0, len(value)):
        print(f"-- {value[j]}")
