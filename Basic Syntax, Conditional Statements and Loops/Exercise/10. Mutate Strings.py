stiring1 = input()
string2 = input()
stiringfinal1 = list(stiring1)
stiringfinal2 = list(string2)

for i in range(0, len(stiring1)):
    if stiring1[i] == string2[i]:
        continue
    else:
        stiringfinal1[i] = stiringfinal2[i]

    final = "".join(stiringfinal1)

    print(final)
