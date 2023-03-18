energy = 100
coins = 100
bool = False
events = input().split("|")

for i in range(len(events)):
    current = events[i]


    current = current.split("-")
    gained = 0


    if current[0] == "rest":
        intitial = energy
        energy = energy + int(current[1])

        if energy > 100:
            energy = 100
            gained = 100 - intitial
        else:
            gained = energy - intitial
        
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")
    elif current[0] == "order":
        if energy - 30 < 0:
            print("You had to rest!")
            energy += 50
            continue
        else:
            coins += int(current[1])
            energy -= 30
            print(f"You earned {current[1]} coins.")
    else:
        if coins - int(current[1]) >= 0:
            coins = coins - int(current[1])
            print(f"You bought {current[0]}.")
        else:
            print(f"Closed! Cannot afford {current[0]}.")
            bool = True
            break
    
if bool == True:
    pass
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
