coffes = input().split()
commands = int(input())
#if it gives an error try on line 13 to give it equal or bigger


for i in range(0, commands):
    command = input().split()

    if command[0] == "Include":
        coffes.append(command[1])

    if command[0] == "Remove":
        if int(command[2]) > len(coffes):
            pass
        elif command[1] == "first":
            for i in range(0, int(command[2])):
                coffes.pop(0)
        elif command[1] == "last":
            for i in range(0, int(command[2])):
                coffes.pop()

    if command[0] == "Prefer":
        if 0 <= int(command[1]) < len(coffes) and  0 <= int(command[2]) < len(coffes):
            a, b = command[1], command[2]
            coffes[int(a)], coffes[int(b)] = coffes[int(b)], coffes[int(a)]
        else:
            pass

    if command[0] == "Reverse":
        coffes.reverse()

final = " ".join(coffes)

print("Coffees:")
print(final)
