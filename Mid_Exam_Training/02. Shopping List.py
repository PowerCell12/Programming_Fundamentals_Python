list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    command = command.split()
    
    if command[0] == "Urgent":
        if command[1] in list:
            pass
        else:
            list.insert(0, command[1])

    if command[0] == "Unnecessary":
        if command[1] in list:
            list.remove(command[1])

    if command[0] == "Correct":
        if command[1] in list:
            position = list.index(command[1])
            list.remove(command[1])
            list.insert(position, command[2])

    if command[0] == "Rearrange":
        if command[1] in list:
            list.remove(command[1])
            list.append(command[1])


list1 = ", ".join(list)

print(list1)
