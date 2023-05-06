commands = input().split("|")
health = 100
amount = 0
counter = 0
all_money = 0

for i in range(0, len(commands)):
    current = commands[i]

    counter += 1

    current = current.split()

    if current[0] == "potion":
        if health == 100:
          amount = 0
          health = 100 
          print(f"You healed for {amount} hp.")
          print(f"Current health: {health} hp.")            
        else:
            amount = int(current[1])
            if health  > 100:
                health = 100
            if health + amount > 100:
                health1 = health + int(current[1])
                amount1 = abs(health1 - 100)
                health = 100
                amount = amount - amount1
            else:
                amount = int(current[1])
                health = health + int(current[1])
            print(f"You healed for {amount} hp.")
            print(f"Current health: {health} hp.") 

    amount = 0

    if current[0] == "chest":
        bitcoins = int(current[1])
        print(f"You found {bitcoins} bitcoins.")
        all_money += bitcoins


    amount = 0

    if current[0] != "chest" and current[0] != "potion":
        attack = int(current[1])
        health = health - attack
        monster = current[0]

        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {counter}")
            break

    if counter == len(commands):
        print(f"You've made it!")
        print(f"Bitcoins: {all_money}")
        print(f"Health: {health}")
