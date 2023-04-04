words = input().split(" ")
new_string = []

for i in range(len(words)):
    current = words[i]
    asci = ""


    for things in current:
        if things.isdigit():
            asci += things
            words[i] = words[i][1:]
        else:
            second = things
            break

    words[i] = chr(int(asci)) + words[i]
    last = words[i][len(words[i]) - 1]

    index1 = words[i].rindex(last)
    index2 = words[i].index(second)

    if index1 == index2:
        new_string.append(words[i])
        continue

    words[i] = words[i].replace(words[i][index2], last, 1)
    words[i]  =  words[i][:-1]  + second

    new_string.append(words[i])


final = " ".join(new_string)
print(final)
