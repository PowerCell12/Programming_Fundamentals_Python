gifts = input().split()

while True:
    commands = input()

    if commands == "No Money":
        break

    commands = commands.split(" ")

    if commands[0] == "OutOfStock":
        if commands[1] in gifts:
            while True:
                if commands[1] not in gifts:
                    break
                final = gifts.index(commands[1])
                gifts[final] = "None"
        else:
            pass
    

    if commands[0] == "Required":
        if -1 < int(commands[2]) < len(gifts):
            gifts.pop(int(commands[2]))
            gifts.insert(int(commands[2]), commands[1])


    if commands[0] == "JustInCase":
            gifts.pop()
            gifts.append(commands[1])

while True:
    if "None" in gifts:
        gifts.remove("None")
    else:
        break



final = " ".join(gifts)

print(final)
