while True:
    strings  = input()
    reversed_str = ""

    if strings == "end":
        break

    for chr in range(len(strings) - 1, -1, - 1):
        reversed_str += strings[chr]

    print(f"{strings} = {reversed_str}")
