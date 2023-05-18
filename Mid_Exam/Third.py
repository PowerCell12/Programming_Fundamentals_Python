phones = input().split(", ")

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" - ")

    if command[0] == "Add":
        if command[1] in phones:
            pass
        else:
            phones.append(command[1])

    if command[0] == "Remove":
        if command[1] in phones:
            phones.remove(command[1])
        else:
            pass
    
    if command[0] == "Bonus phone":
        final = command[1].split(":")
    
        if final[0] in phones:
            index = phones.index(final[0]) + 1
            phones.insert(index, final[1])
        else:
            pass

    if command[0] == "Last":
        if command[1] in phones:
            final5  = command[1]
            final1 = phones.remove(command[1])
            phones.append(final5)
        else:
            pass

final3 = ", ".join(phones)
print(final3)

# 100/100
