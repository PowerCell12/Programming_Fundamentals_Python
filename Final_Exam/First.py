  spell = input()

while True:

    commands = input().split()

    if commands[0] == "Abracadabra":
        break

    if commands[0] == "Abjuration":

        spell = spell.upper()
        print(spell)

    elif commands[0] == "Necromancy":

        spell = spell.lower()
        print(spell)

    elif commands[0] == "Illusion":

        if int(commands[1]) < 0 or int(commands[1]) >= len(spell):
            print("The spell was too weak.")
            continue

        spell = spell[:int(commands[1])] + commands[2] + spell[int(commands[1]) + 1:]

        print("Done!")

    elif commands[0] == "Divination":

        if commands[1] in spell:
            
            spell = spell.replace(commands[1], commands[2])
            print(spell)


    elif commands[0] == "Alteration":
        if commands[1] in spell:
            ## if error , do , 1   in replace
            spell = spell.replace(commands[1], "")
            print(spell)

    else:
        print("The spell did not work!")
