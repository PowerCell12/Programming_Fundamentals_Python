string = input().split(" ")
characters = {}

for i in string:

    for j in i:
        if j == " ":
            continue

        if j not in characters:
            characters[j] = 1
        else:
            characters[j] = int(characters[j] + 1)

for key, value in characters.items():
    print(f"{key} -> {value}")
