string = input()
new_string = ""
prev_char = ""

for i, char in enumerate(string):
    if char != prev_char:
        new_string += char
        prev_char = char
    elif i == len(string) - 1:
        new_string = new_string[:-1] + char
    else:
        continue

print(new_string)
