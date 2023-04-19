keys = input().split(" ")
counter = 0
new_strings = ""
index1 = 0
index2 = 0
index3 = 0
index4 = 0

while True:
    commands = input()

    if commands == "find":
        break

    for i in range(len(commands)):
        current = commands[i]

        final = ord(current)

        if counter >= len(keys):
            counter = 0

        final_1 = final - int(keys[counter])

        final_2 = chr(final_1)


        new_strings += final_2

        counter += 1
    
    index1 = new_strings.index("&")
    index2 = new_strings.rindex("&")
    index3 = new_strings.index("<")
    index4 = new_strings.index(">")

    typeMatirial = new_strings[index1 + 1:index2]
    cordinaties = new_strings[index3 + 1:index4]

    print(f"Found {typeMatirial} at {cordinaties}")

    counter = 0
    new_strings = ""
