command = input()
whatever = input()
final = 0


def datatypes(command, whatever, final):
    if command == "int":
        final = int(whatever) * 2
        print(final) 
    elif command == "real":
        final = float(whatever) * 1.5
        print(f"{final:.2f}")
    elif command == "string":
        final = whatever
        print(f"${final}$")

datatypes(command, whatever, final)
