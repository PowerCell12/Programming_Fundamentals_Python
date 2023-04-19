strings = input().split(" ")
new_strings = ""
letter = ""

for command in strings:
    
        if command == "":
            continue

        if command == "|":
            letter = " "

        if command == ".-":
            letter = "A"

        if command == "-...":
            letter = "B"

        if command == "-.-.":
            letter = "C"

        if command == "-..":
            letter = "D"

        if command == ".":
            letter = "E"

        if command == "..-.":
            letter = "F"

        if command == "--.":
            letter = "G"

        if command == "....":
            letter = "H"

        if command == "..":
            letter = "I"

        if command == ".---":
            letter = "J"

        if command == "-.-":
            letter = "K"

        if command == ".-..":
            letter = "L"

        if command == "--":
            letter = "M"

        if command == "-.":
            letter = "N"

        if command == "---":
            letter = "O"

        if command == ".--.":
            letter = "P"

        if command == "--.-":
            letter = "Q"
    
        if command == ".-.":
            letter = "R"

        if command == "...":
            letter = "S"

        if command == "-":
            letter = "T"

        if command == "..-":
            letter = "U"

        if command == "...-":
            letter = "V"

        if command == ".--":
            letter = "W"

        if command == "-..-":
            letter = "X"
    
        if command == "-.--":
            letter = "Y"

        if command == "--..":
            letter = "Z"


        new_strings += letter

print(new_strings)
