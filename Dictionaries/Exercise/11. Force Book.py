ForceSide_ForceUser  = {}
list1 = []
final = 0
which = ""

while True:
    commands = input()

    if commands == 'Lumpawaroo':
        break

    if '|' in commands:
        commands = commands.split(' | ')

        if commands[1] not in list1 and commands[0] in ForceSide_ForceUser.keys():
            if commands[0] in ForceSide_ForceUser.keys():
                ForceSide_ForceUser[commands[0]].append(commands[1])
                list1.append(commands[1])
                continue

        if commands[1] not in list1:
            if commands[0] not in ForceSide_ForceUser.keys():
                ForceSide_ForceUser[commands[0]] = []
                ForceSide_ForceUser[commands[0]].append(commands[1])
                list1.append(commands[1])
                continue

    else:
        commands = commands.split(" -> ")

        if commands[0] not in list1 and commands[1] in ForceSide_ForceUser.keys():
            ForceSide_ForceUser[commands[1]].append(commands[0])
            list1.append(commands[0])

            print(f"{commands[0]} joins the {commands[1]} side!")

            continue


        if commands[0] not in list1 and commands[1] not in ForceSide_ForceUser.keys():
            ForceSide_ForceUser[commands[1]] = []
            ForceSide_ForceUser[commands[1]].append(commands[0])
            list1.append(commands[0])

            print(f"{commands[0]} joins the {commands[1]} side!")

            continue

        if commands[0] in list1:
            for key, value in ForceSide_ForceUser.items():
                if commands[0] in value:
                    value.remove(commands[0])
                    final = commands[0]
                    which  = key

            for key, value in ForceSide_ForceUser.items():
                if key != which:
                    value.append(final)

            print(f"{commands[0]} joins the {commands[1]} side!")

            continue



for key, value in ForceSide_ForceUser.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in value:
            print(f"! {i}")
