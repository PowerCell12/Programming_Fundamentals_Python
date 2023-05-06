journal = input().split(", ")

while True:
    command = input().split(" - ")

    if command[0] == "Craft!":
        break

    if command[0] == "Collect" and command[1] not in journal:
        journal.append(command[1])

    if command[0] == "Drop" and command[1] in journal:
        journal.remove(command[1])

    if command[0] == "Renew" and command[1] in journal:
        last_place = journal.remove(command[1])
        journal.append(command[1])

    check = command[1].split(":")

    if command[0] == "Combine Items" and check[0] in journal:
        index = journal.index(check[0]) + 1
        journal.insert(index, check[1])


final = ", ".join(journal)

print(final)
