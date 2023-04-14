strings = input()
digits = ""
letters = ""
charactr = ""


for ch in strings:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        charactr += ch

print(digits)
print(letters)
print(charactr)
