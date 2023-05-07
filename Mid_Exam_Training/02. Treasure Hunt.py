items = input().split("|")
counter = 0
all = 0

while True:
    command = input()

    if command == "Yohoho!":
        break

    command = command.split()

    if command[0] == "Loot":
        for i in range(0, len(command)):
            counter += 1
            index = len(command)
            if counter >= index:
                break
            if command[counter] not in items:
                items.insert(0, command[counter])
    counter  = 0

    if command[0] == "Drop":
        if int(command[1]) >= len(items):
            pass
        else:
            item_pop = items.pop(int(command[1]))
            items.append(item_pop)

    if command[0] == "Steal":
        if int(command[1]) >= len(items):
            final = ", ".join(items)
            print(final)
            for i in range(0, len(items)):
                items.clear()
        else:
                to_print = -1 * int(command[1])
                the_slice = items[to_print:len(items)]
                final = ", ".join(the_slice)
                print(final)
                items = items[0:to_print]

if len(items) <= 0:
    print("Failed treasure hunt.")
else:
    for i in range(0, len(items)):
        current  = items[i]

        average = len(current)

        all += average

    final_done = all / len(items)
    print(f"Average treasure gain: {final_done:.2f} pirate credits.")
