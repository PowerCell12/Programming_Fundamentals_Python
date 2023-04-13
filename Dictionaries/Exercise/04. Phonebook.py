PhoneBook = {}

while True:
    NameAndNumber  = input().split("-")

    if NameAndNumber[0].isdigit():
        break

    key = NameAndNumber[0]
    value = NameAndNumber[1]


    PhoneBook[key] = value

lines = NameAndNumber[0]

for i in range(int(lines)):

    Name = input()

    if Name in PhoneBook.keys():
            print(f"{Name} -> {PhoneBook[Name]}")
    else:
        print(f"Contact {Name} does not exist.")
