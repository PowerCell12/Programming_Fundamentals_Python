string = input()
list = string.split(", ")
wolfposition = 0


for i in range(0, len(list)):
    if list[i] == "wolf":
        wolfposition = i
        break

sheepostion = wolfposition + 1

sheepostion = len(list) - sheepostion

if list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheepostion}! You are about to be eaten by a wolf!")
