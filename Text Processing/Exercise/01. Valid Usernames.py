words = input().split(", ")
symbols = "!@#$%^&*()+?=,<>/"

for word in words:
    counter1 = 0
    counter2 = 0

    if 3 < len(word) < 17:
        pass
    else:
        continue

    for chr in word:
        if chr == " ":
            counter1 += 1
            break

    if counter1 == 1:
        continue


    for chrk in symbols:
        if chrk in word:
            counter2 += 1
            break

    if counter2 == 1:
        continue

    print(word, end="\n")
