to_remove = input()
strings = input()

for i in range(0, len(strings)):
    if to_remove in strings:
        strings = strings.replace(to_remove, "")
    else:
        break
print(strings)
